# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Multp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(227, 112)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Op1 = QtWidgets.QLineEdit(self.centralwidget)
        self.Op1.setGeometry(QtCore.QRect(10, 40, 41, 20))
        self.Op1.setObjectName("Op1")
        self.Op2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Op2.setGeometry(QtCore.QRect(100, 40, 41, 20))
        self.Op2.setObjectName("Op2")
        self.Fixo = QtWidgets.QLabel(self.centralwidget)
        self.Fixo.setGeometry(QtCore.QRect(70, 40, 21, 16))
        self.Fixo.setScaledContents(False)
        self.Fixo.setAlignment(QtCore.Qt.AlignCenter)
        self.Fixo.setObjectName("Fixo")
        self.Resultado = QtWidgets.QLabel(self.centralwidget)#instancia o objeto da frame
        self.Resultado.setGeometry(QtCore.QRect(160, 40, 41, 16))#fala as dimensões do objeto
        self.Resultado.setObjectName("Resultado")#seta o valor do objeto
        self.Operar = QtWidgets.QPushButton(self.centralwidget)
        self.Operar.setGeometry(QtCore.QRect(70, 80, 75, 23))
        self.Operar.setObjectName("Operar")
        self.Operar.clicked.connect(self.operador)#quando clicado, executa a função operador
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Fixo.setText(_translate("MainWindow", "X"))
        self.Resultado.setText(_translate("MainWindow", "="))
        self.Operar.setText(_translate("MainWindow", "Operar"))
    
    def operador(self):
        
        n1 = float(self.Op1.text())
        n2 = float(self.Op2.text())#pega o texto do editor de linha
        self.Resultado.setText(str(n1*n2))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
