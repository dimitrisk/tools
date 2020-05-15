"""
/***************************************************************************
Centroids
A QGIS plugin
Make centroids of polygons
                             -------------------
begin                : 2009-04-14
copyright            : (C) 2009 by Dimitris Kavroudakis, with ideas and code
                        from fTools (Copyright (c) 2009 Carson J. Q. Farmer)
URL                  : www.dimitrisk.gr
 ***************************************************************************/

/***************************************************************************
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
*****************************************************************************/
"""
from PyQt4 import QtCore, QtGui
from qgis.core import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

from Ui_Centroids import Ui_Centroids
# create the dialog for Centroids
class CentroidsDialog(QtGui.QDialog):
    def __init__(self,iface):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.iface = iface
        self.ui = Ui_Centroids ()
        
        self.ui.setupUi(self)

        QObject.connect(self.ui.comboBox, SIGNAL("currentIndexChanged(QString)"), self.update)
        QObject.connect(self.ui.brownseButton, SIGNAL("clicked()"), self.outFile)
        QObject.connect(self.ui.stop_button, SIGNAL("clicked()"), self.close)
        QObject.connect(self.ui.run_Button, SIGNAL("clicked()"), self.accept)

        self.success = False
        self.manageGui()

    def manageGui(self):
      myList = []
      self.ui.comboBox.clear()
      myList = self.getLayerNames( [ QGis.Polygon ] )
      self.ui.comboBox.addItems( myList )
      return



    #overide
    def accept(self):
        if self.ui.comboBox.currentText() == "":
            QMessageBox.information(self, "Error", self.tr( "Please specify input vector layer" ) )
        if self.ui.outLineEdit.text() == "":
            QMessageBox.information(self, "Error", self.tr( "Please specify output shapefile" ) )
        else:
            self.do(self.ui.comboBox.currentText(),self.ui.outLineEdit.text())

    def do(self,myLayer,inName):
        vlayer = self.getVectorLayerByName(myLayer )

        self.testThread = GeometryThread( self.iface.mainWindow(), self, vlayer,inName, self.encoding )
        QObject.connect( self.testThread, SIGNAL( "runFinished(PyQt_PyObject)" ), self.after )
        self.ui.stop_button.setText( "Cancel Thread" )
        QObject.connect( self.ui.stop_button, SIGNAL( "clicked()" ), self.cancelThread )
        self.testThread.start()
        
    def cancelThread( self ):
		self.testThread.stop()
        
    def after( self, success ):
		self.testThread.stop()
		if success == "math_error":
			QMessageBox.warning( self, "Geometry", self.tr( "Error processing specified tolerance!" ) + "\n"
			+ self.tr( "Please choose larger tolerance..." ) )
			if not QgsVectorFileWriter.deleteShapeFile( self.shapefileName ):
				QMessageBox.warning( self, "Geometry", self.tr( "Unable to delete incomplete shapefile." ) )
		else:
			self.ui.stop_button.setText( "Close" )
			QObject.disconnect( self.ui.stop_button, SIGNAL( "clicked()" ), self.cancelThread )
			if success:
				addToTOC = QMessageBox.question( self, "Geometry", self.tr( "Created output shapefile:" ) + "\n" +
				unicode( self.shapefileName ) + "\n\n" + self.tr( "Add the new layer to the TOC?" ),
				QMessageBox.Yes, QMessageBox.No, QMessageBox.NoButton )
				if addToTOC == QMessageBox.Yes:
					self.addShapeToCanvas( unicode( self.shapefileName ) )
			else:
				QMessageBox.warning( self, "Geometry", self.tr( "Error writing output shapefile." ) )        

# Return list of names of all layers in QgsMapLayerRegistry
    def getLayerNames(self, vTypes ):
        layermap = QgsMapLayerRegistry.instance().mapLayers()
        layerlist = []
        if vTypes == "all":
            for name, layer in layermap.iteritems():
                layerlist.append( unicode( layer.name() ) )
        else:
            for name, layer in layermap.iteritems():
                if layer.type() == QgsMapLayer.VectorLayer:
                    if layer.geometryType() in vTypes:
                        layerlist.append( unicode( layer.name() ) )
        return layerlist
    
# Convinience function to add a vector layer to canvas based on input shapefile path ( as string )
    def addShapeToCanvas(self, shapeFilePath ):
        shapeFilePathList = shapeFilePath.split( "/" )
        layerName = QString( shapeFilePathList[len(shapeFilePathList)-1] )
        if layerName.endsWith( ".shp" ):
            layerName = unicode( layerName ).rstrip( ".shp" )
        vlayer_new = QgsVectorLayer( shapeFilePath, layerName, "ogr" )

        if vlayer_new.isValid():
            QgsMapLayerRegistry.instance().addMapLayer(vlayer_new)
            return True
        else:
            return False
    
# Return QgsVectorLayer from a layer name ( as string )
    def getVectorLayerByName( self, myName ):
        layermap = QgsMapLayerRegistry.instance().mapLayers()
        for name, layer in layermap.iteritems():
            if layer.type() == QgsMapLayer.VectorLayer and layer.name() == myName:
                if layer.isValid():
                    return layer
                else:
                    return None

    def outFile(self):
		self.ui.outLineEdit.clear()
		(self.shapefileName, self.encoding) = self.saveDialog(self)
		if self.shapefileName is None or self.encoding is None:
			return
		self.ui.outLineEdit.setText(QString(self.shapefileName))

    def saveDialog(self, parent ):
        settings = QSettings()
        dirName = settings.value( "/UI/lastShapefileDir" ).toString()
        filtering = QString( "Shapefiles (*.shp)" )
        encode = settings.value( "/UI/encoding" ).toString()
        fileDialog = QgsEncodingFileDialog( parent, "Save output shapefile", dirName, filtering, encode )
        fileDialog.setDefaultSuffix( QString( "shp" ) )
        fileDialog.setFileMode( QFileDialog.AnyFile )
        fileDialog.setAcceptMode( QFileDialog.AcceptSave )
        fileDialog.setConfirmOverwrite( True )
        if not fileDialog.exec_() == QDialog.Accepted:
                return None, None
        files = fileDialog.selectedFiles()
        settings.setValue("/UI/lastShapefileDir", QVariant( QFileInfo( unicode( files.first() ) ).absolutePath() ) )
        return ( unicode( files.first() ), unicode( fileDialog.encoding() ) )

class GeometryThread( QThread ):
	def __init__( self, parentThread, parentObject, vlayer, myInName, myEncoding ):
		QThread.__init__( self, parentThread )
		self.parent = parentObject
		self.running = False
		self.vlayer = vlayer
		self.myName = myInName
		self.myEncoding = myEncoding

	def run( self ):
		self.running = True
		success = self.polygon_centroids()
		self.emit( SIGNAL( "runFinished(PyQt_PyObject)" ), success )
		self.emit( SIGNAL( "runStatus(PyQt_PyObject)" ), 0 )

	def stop(self):
		self.running = False

	def polygon_centroids( self ):
		vprovider = self.vlayer.dataProvider()
		allAttrs = vprovider.attributeIndexes()
		vprovider.select( allAttrs )
		fields = vprovider.fields()
		writer = QgsVectorFileWriter( self.myName, self.myEncoding,fields,QGis.WKBPoint, vprovider.crs() )
		inFeat = QgsFeature()
		outfeat = QgsFeature()
		nFeat = vprovider.featureCount()
		nElement = 0
		self.emit( SIGNAL( "runStatus(PyQt_PyObject)" ), 0 )
		self.emit( SIGNAL( "runRange(PyQt_PyObject)" ), ( 0, nFeat ) )
		while vprovider.nextFeature( inFeat ):
			geom = inFeat.geometry()
			area = QgsDistanceArea()
			A = area.measure( geom )
			multi_geom = QgsGeometry()
			bounding = inFeat.geometry().boundingBox()
			xmin = bounding.xMinimum()
			ymin = bounding.yMinimum()
			xmax = bounding.xMaximum()
			ymax = bounding.yMaximum()
			if geom.type() == 2:
				cx = 0
				cy = 0
				area2 = 0
				if geom.isMultipart():
					multi_geom = geom.asMultiPolygon()
					for k in multi_geom:
						for h in k:
							for i in range(0, len(h) - 1):
								j = (i + 1) % len(h)
								factor = ((h[i].x()-xmin) * (h[j].y()-ymin) - (h[j].x()-xmin) * (h[i].y()-ymin))
								cx = cx + ((h[i].x()-xmin) + (h[j].x()-xmin)) * factor
								cy = cy + ((h[i].y()-ymin) + (h[j].y()-ymin)) * factor
				else:
					multi_geom = geom.asPolygon()
					for k in multi_geom:
						for i in range(0, len(k) - 1):
							j = (i + 1) % len(k)
							factor = (k[i].x()-xmin) * (k[j].y()-ymin) - (k[j].x()-xmin) * (k[i].y()-ymin)
							cx = cx + ((k[i].x()-xmin) + (k[j].x()-xmin)) * factor
							cy = cy + ((k[i].y()-ymin) + (k[j].y()-ymin)) * factor
				A = A * (-6)
				factor = 1/A
				cx = cx * factor
				cy = cy * factor
				cx = cx + xmin
				cy = cy + ymin
				outfeat.setGeometry( QgsGeometry.fromPoint( QgsPoint( cx, cy ) ) )
				atMap = inFeat.attributeMap()
				outfeat.setAttributeMap( atMap )
				writer.addFeature( outfeat )
			nElement += 1
			self.emit( SIGNAL( "runStatus(PyQt_PyObject)" ),  nElement )
		del writer
		return True
    