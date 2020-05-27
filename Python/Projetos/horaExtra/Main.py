from frontend.Interface import QtWidgets, Ui_timeSet
from frontend.mensagem import Ui_mensagem
from backend import Cadastros, Doc

#=-=-=-=-=-Estâncias e configurações=-=-=-=-=-=-=
import sys
app = QtWidgets.QApplication(sys.argv)
mainForm = QtWidgets.QWidget()
msgForm = QtWidgets.QWidget()
uiMSG = Ui_mensagem()
uiMain = Ui_timeSet()
uiMSG.setupUi(msgForm)
uiMain.setupUi(mainForm)
mainForm.show()
#=-=-=-=-=-=-=-=-=-=-=-=

def buscar():
    
    nome = uiMain.lineEdit_Nome.text()
    func = Cadastros.dadosFunc(nome)
    if func != -1:
        uiMain.label_Nome.setText(func[0])
        uiMain.label_CPF.setText(str(func[1]))
        uiMain.label_Cargo.setText(func[2])
        uiMain.label_Salario.setText(f'R$ {func[3]:.2f}')
        uiMain.label_HoraExtra.setText(str(func[4]))
        uiMain.label_PagExtra.setText(f'R$ {Valorhr(func[3],func[4]):.2f}')
    else:
        uiMSG.label_msg.setText("Funcionário não encontrado")
        msgForm.show()
def inserirHora():
    try:
        cpf = int(uiMain.label_CPF.text())
    except:
        uiMSG.label_msg.setText("Identifique o funcionário")
        msgForm.show()
        return
    try:
        hora = int(uiMain.lineEdit_HoraExtra.text())
    except:
        uiMSG.label_msg.setText("Hora inválida")
        msgForm.show()
        return
    Doc.attHora(cpf, hora)
    buscar()

def Valorhr(salario, tempo):
    return (salario/180)*1.5*tempo

def ui_cadFunc():
    pass
    
uiMain.pushButton_novoFunc.clicked.connect(ui_cadFunc)
uiMain.pushButton_Buscar.clicked.connect(buscar)
uiMain.pushButton_InsereHE.clicked.connect(inserirHora)
app.exec_()