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

class Ui_Centroids(object):
    def setupUi(self, Centroids):
        Centroids.setObjectName("Centroids")
        Centroids.resize(351,143)
        self.gridLayout = QtGui.QGridLayout(Centroids)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Centroids)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label,0,0,1,1)
        self.comboBox = QtGui.QComboBox(Centroids)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox,1,0,1,4)
        self.label_2 = QtGui.QLabel(Centroids)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2,2,0,1,1)
        self.outLineEdit = QtGui.QLineEdit(Centroids)
        self.outLineEdit.setObjectName("outLineEdit")
        self.gridLayout.addWidget(self.outLineEdit,3,0,1,3)
        self.brownseButton = QtGui.QPushButton(Centroids)
        self.brownseButton.setObjectName("brownseButton")
        self.gridLayout.addWidget(self.brownseButton,3,3,1,1)
        self.stop_button = QtGui.QPushButton(Centroids)
        self.stop_button.setObjectName("stop_button")
        self.gridLayout.addWidget(self.stop_button,4,3,1,1)
        self.run_Button = QtGui.QPushButton(Centroids)
        self.run_Button.setObjectName("run_Button")
        self.gridLayout.addWidget(self.run_Button,4,2,1,1)

        self.retranslateUi(Centroids)
        QtCore.QMetaObject.connectSlotsByName(Centroids)

    def retranslateUi(self, Centroids):
        Centroids.setWindowTitle(QtGui.QApplication.translate("Centroids", "Centroids Maker - Dimitris Kavroudakis", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Centroids", "Select a polygon layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Centroids", "Output Shapefile", None, QtGui.QApplication.UnicodeUTF8))
        self.brownseButton.setText(QtGui.QApplication.translate("Centroids", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.stop_button.setText(QtGui.QApplication.translate("Centroids", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.run_Button.setText(QtGui.QApplication.translate("Centroids", "Run", None, QtGui.QApplication.UnicodeUTF8))

