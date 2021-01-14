
from calculator import Ui_MainWindow
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.text=" "
        self.ui.label.setText(self.text)
        self.ui.pushButton.clicked.connect(self.buttonClicked)
        self.ui.pushButton_2.clicked.connect(self.buttonClicked)
        self.ui.pushButton_3.clicked.connect(self.buttonClicked)
        self.ui.pushButton_4.clicked.connect(self.buttonClicked)
        self.ui.pushButton_5.clicked.connect(self.buttonClicked)
        self.ui.pushButton_6.clicked.connect(self.buttonClicked)
        self.ui.pushButton_7.clicked.connect(self.buttonClicked)
        self.ui.pushButton_8.clicked.connect(self.buttonClicked)
        self.ui.pushButton_9.clicked.connect(self.buttonClicked)
        self.ui.pushButton_10.clicked.connect(self.buttonClicked)
        self.ui.pushButton_11.clicked.connect(self.buttonClicked)
        self.ui.pushButton_12.clicked.connect(self.buttonClicked)
        self.ui.pushButton_13.clicked.connect(self.buttonClicked)
        self.ui.pushButton_14.clicked.connect(self.buttonClicked)
        self.ui.pushButton_15.clicked.connect(self.buttonClicked)
        self.ui.pushButton_16.clicked.connect(self.buttonClicked)
        self.ui.pushButton_18.clicked.connect(self.buttonClicked)
        self.ui.pushButton_19.clicked.connect(self.buttonClicked)
        self.ui.pushButton_20.clicked.connect(self.buttonClicked)
        self.ui.pushButton_21.clicked.connect(self.buttonClicked)
    def buttonClicked(self):
        button=self.sender()
        self.text=self.ui.label.text()
        if "=" in self.text or "Wrong Syntax" in self.text:
            self.text=" "
            self.ui.label.setText(self.text)
        if button.text()=="=":
            try:
                value_=eval(self.text)
                self.ui.label.setText(self.text+" = "+str(value_))
            except SyntaxError:
                self.ui.label.setText("  Wrong Syntax")
        elif "<" in button.text():
            len_=len(button.text())
            self.text=self.text[:-len_]
            self.ui.label.setText(self.text)
        else:
            self.ui.label.setText(self.text+button.text())
    
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())




