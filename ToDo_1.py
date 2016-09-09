#ToDo Python file
import sys
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("todo_menu.ui")[0]

class ToDoMenuClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
#        self.addTodobtn.clicked.connect(self.addTodobtn_clicked)
        self.actionExit.triggered.connect(self.menuExit_selected)
    
    def addTodobtn_clicked(self):
        todoItem = str(self.ToDoAddItem.text())
        self.item.setText(str(todoItem))

        
    def menuExit_selected(self):
        self.close()
        
app = QtGui.QApplication(sys.argv)
myWindow = ToDoMenuClass(None)
myWindow.show()
app.exec_()
    