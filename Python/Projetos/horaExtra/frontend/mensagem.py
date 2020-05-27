# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mensagem.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mensagem(object):
    def setupUi(self, mensagem):
        mensagem.setObjectName("mensagem")
        mensagem.setWindowModality(QtCore.Qt.WindowModal)
        mensagem.setEnabled(True)
        mensagem.resize(392, 61)
        mensagem.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setItalic(False)
        mensagem.setFont(font)
        mensagem.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_msg = QtWidgets.QLabel(mensagem)
        self.label_msg.setGeometry(QtCore.QRect(10, 10, 371, 41))
        self.label_msg.setBaseSize(QtCore.QSize(5, 5))
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_msg.setFont(font)
        self.label_msg.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_msg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_msg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_msg.setObjectName("label_msg")

        self.retranslateUi(mensagem)
        QtCore.QMetaObject.connectSlotsByName(mensagem)

    def retranslateUi(self, mensagem):
        _translate = QtCore.QCoreApplication.translate
        mensagem.setWindowTitle(_translate("mensagem", "Erro!"))
        self.label_msg.setText(_translate("mensagem", ""))