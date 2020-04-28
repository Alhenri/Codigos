# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import serial


def config_USB(porta):
    try:
        global arduino
        arduino = serial.Serial(porta, 9600, timeout=1)#timeout é o tempo de tolerancia, tanto pra enviar, quanto pra receber
        while not arduino.isOpen():
            pass
    except:
        arduino = serial.Serial('COM5', 9600, timeout=1)
        print('Porta inexistente ou ocupada!')
def send_msg(msg):
    try:
        global arduino
        arduino.write(msg.encode())
        #print(arduino.readline()) #se receber algo ele mostra tudo até o \n
    except:
        print('Porta não configurada')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(230, 164)
        MainWindow.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_portas = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_portas.setGeometry(QtCore.QRect(128, 10, 91, 21))
        self.comboBox_portas.activated.connect(self.pegaId)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_portas.setFont(font)
        self.comboBox_portas.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_portas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_portas.setObjectName("comboBox_portas")
        self.comboBox_portas.addItem("")
        self.comboBox_portas.addItem("")
        self.comboBox_portas.addItem("")
        self.comboBox_portas.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        #---------------------------------------------------------------
        self.pushButton_c1On = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_c1On.setGeometry(QtCore.QRect(130, 70, 41, 23))
        self.pushButton_c1On.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_c1On.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_c1On.setDefault(False)
        self.pushButton_c1On.setFlat(False)
        self.pushButton_c1On.setObjectName("pushButton_c1On")
        self.pushButton_c1On.clicked.connect(self.comando01_On)
        #---------------------------------------------------------------
        self.pushButton_c1Off = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_c1Off.setGeometry(QtCore.QRect(180, 70, 41, 23))
        self.pushButton_c1Off.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_c1Off.setObjectName("pushButton_c1Off")
        self.pushButton_c1Off.clicked.connect(self.comando01_Off)
        #---------------------------------------------------------------
        self.pushButton_c2Off = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_c2Off.setGeometry(QtCore.QRect(180, 100, 41, 23))
        self.pushButton_c2Off.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_c2Off.setObjectName("pushButton_c2Off")
        self.pushButton_c2Off.clicked.connect(self.comando02_Off)
        #---------------------------------------------------------------
        self.pushButton_c2On = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_c2On.setGeometry(QtCore.QRect(130, 100, 41, 23))
        self.pushButton_c2On.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_c2On.setObjectName("pushButton_c2On")
        self.pushButton_c2On.clicked.connect(self.comando02_On)
        #---------------------------------------------------------------
        self.pushButton_c3Off = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_c3Off.setGeometry(QtCore.QRect(180, 130, 41, 23))
        self.pushButton_c3Off.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_c3Off.setObjectName("pushButton_c3Off")
        self.pushButton_c3Off.clicked.connect(self.comando03_Off)
        #---------------------------------------------------------------
        self.pushButton_c3On = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_c3On.setGeometry(QtCore.QRect(130, 130, 41, 23))
        self.pushButton_c3On.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_c3On.setObjectName("pushButton_c3On")
        self.pushButton_c3On.clicked.connect(self.comando03_On)
        #---------------------------------------------------------------
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def pegaId(self, index):
        #posso pegar tanto otextp (itemText) como o dado (itemData)
        config_USB(self.comboBox_portas.itemText(index))
    
    def comando01_On(self):
        send_msg('A')
    
    def comando01_Off(self):
        send_msg('a')
    
    def comando02_On(self):
        send_msg('B')
    
    def comando02_Off(self):
        send_msg('b')
    
    def comando03_On(self):
        send_msg('C')
    
    def comando03_Off(self):
        send_msg('c')
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Teste Serial"))
        self.comboBox_portas.setCurrentText(_translate("MainWindow", "COM0"))
        self.comboBox_portas.setItemText(0, _translate("MainWindow", "COM0"))
        self.comboBox_portas.setItemText(1, _translate("MainWindow", "COM1"))
        self.comboBox_portas.setItemText(2, _translate("MainWindow", "COM2"))
        self.comboBox_portas.setItemText(3, _translate("MainWindow", "COM3"))
        self.label.setText(_translate("MainWindow", "Porta Serial :"))
        self.label_2.setText(_translate("MainWindow", "Comando 01:"))
        self.label_3.setText(_translate("MainWindow", "Comando 02:"))
        self.label_4.setText(_translate("MainWindow", "Comando 03:"))
        self.pushButton_c1On.setText(_translate("MainWindow", "On"))
        self.pushButton_c1Off.setText(_translate("MainWindow", "Off"))
        self.pushButton_c2Off.setText(_translate("MainWindow", "Off"))
        self.pushButton_c2On.setText(_translate("MainWindow", "On"))
        self.pushButton_c3Off.setText(_translate("MainWindow", "Off"))
        self.pushButton_c3On.setText(_translate("MainWindow", "On"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
