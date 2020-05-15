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

from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
import resources
from CentroidsDialog import CentroidsDialog

class Centroids: 

  def __init__(self, iface):
    # Save reference to the QGIS interface
    self.iface = iface

  def initGui(self):  
    # Create action that will start plugin configuration
    self.action = QAction(QIcon(":/plugins/centroids/icon.png"), \
        "Centroids Maker", self.iface.mainWindow())
    # connect the action to the run method
    QObject.connect(self.action, SIGNAL("activated()"), self.run) 

    # Add toolbar button and menu item
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&Centroids Maker", self.action)

  def unload(self):
    # Remove the plugin menu item and icon
    self.iface.removePluginMenu("&Centroids Maker",self.action)
    self.iface.removeToolBarIcon(self.action)

  # run method that performs all the real work
  def run(self): 
    # create and show the dialog 
    dlg = CentroidsDialog(self.iface)
    # show the dialog
    dlg.show()
    result = dlg.exec_()
