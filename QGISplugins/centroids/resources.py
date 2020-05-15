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
from PyQt4 import QtCore

qt_resource_data = "\
\x00\x00\x00\xbb\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x20\x00\x00\x00\x20\x02\x03\x00\x00\x00\x0e\x14\x92\x67\
\x00\x00\x00\x01\x73\x52\x47\x42\x00\xae\xce\x1c\xe9\x00\x00\x00\
\x09\x50\x4c\x54\x45\x00\x00\x00\x30\x30\x30\x80\x80\x80\xe1\x1d\
\xae\xa1\x00\x00\x00\x01\x74\x52\x4e\x53\x00\x40\xe6\xd8\x66\x00\
\x00\x00\x53\x49\x44\x41\x54\x18\xd3\x63\x60\x20\x0a\x30\xad\x80\
\x32\x34\x60\xac\x06\xa8\x18\x13\x14\x33\x70\x40\x44\x19\x18\x14\
\x60\x8c\x06\x06\x16\x24\x86\x02\x12\x03\xa8\x01\xc6\x60\x0d\x0d\
\x01\x69\x85\x88\x30\xc1\xd4\xa0\x30\x14\x40\x0c\x90\x41\x1c\x50\
\x9b\xb1\x30\x98\x90\xdc\xc2\xb5\x6a\x05\x44\x54\x01\xe2\x54\xad\
\x55\x0d\x0c\xe4\x02\x00\xfc\xa0\x0d\xa3\x43\x27\xd9\xcf\x00\x00\
\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82\
"

qt_resource_name = "\
\x00\x07\
\x07\x3b\xe0\xb3\
\x00\x70\
\x00\x6c\x00\x75\x00\x67\x00\x69\x00\x6e\x00\x73\
\x00\x09\
\x05\xb9\x8c\x33\
\x00\x63\
\x00\x65\x00\x6e\x00\x74\x00\x72\x00\x6f\x00\x69\x00\x64\x00\x73\
\x00\x08\
\x0a\x61\x5a\xa7\
\x00\x69\
\x00\x63\x00\x6f\x00\x6e\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct = "\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x14\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x2c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
