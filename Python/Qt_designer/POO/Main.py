from PyQt5 import QtCore, QtGui, QtWidgets
from Frame1 import Ui_MainWindow
from Frame2 import Ui_Form
import sys

def printar():
    print('Funciona')
    Form.show()
def setText():
    f2.label.setText("Apertei")
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
Form = QtWidgets.QWidget()
ui = Ui_MainWindow()
f2 = Ui_Form()
ui.setupUi(MainWindow)
f2.setupUi(Form)
MainWindow.show()
ui.pushButton_c1On.clicked.connect(printar)
f2.pushButton.clicked.connect(setText)
app.exec_()