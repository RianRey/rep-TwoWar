import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(300, 300)
widget.setWindowTitle('Main')
widget.show()

sys.exit(app.exec_())
