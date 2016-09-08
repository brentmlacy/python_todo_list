#ToDo Python file
import sys
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("todo_menu.ui")[0]

class ToDoMenu(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.Add_ToDo_item_button.clicked.connect(self.Add_ToDo_button_clicked)
        self.actionExit.triggered.connect(self.menuExit_selected)
    def Add_ToDo_button_clicked(self):
        todo_Item = str(self.ToDo_Add_Item())
        
        
app = QtGui.QApplication(sys.argv)
myapp = ToDoMenu()
myapp.show()
app.exec_()
    