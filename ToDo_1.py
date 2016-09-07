#ToDo Python file
import sys
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("todo_menu.ui")[0]

class ToDoMenu(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setup.Ui(self)
        self.Add_ToDo_Item_button.clicked.connect(self.Add_ToDo_Item_button_clicked)

app = QtGui.QApplication(sys.argv)
myapp = ToDoMenu(None)
myapp.show()
app.exec_()
    