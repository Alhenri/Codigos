from frontend.Interface import QtWidgets, Ui_Form
from backend import Cadastros, Doc
import sys
#=-=-=-=-=-=-=-=-=-=-=-=
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
#=-=-=-=-=-=-=-=-=-=-=-=

def buscar():
    
    nome = ui.lineEdit_Nome.text()
    func = Cadastros.dadosFunc(nome)
    cpf = func[4]
    ui.label_Nome.setText(func[0])
    ui.label_CPF.setText(str(func[1]))
    ui.label_Cargo.setText(func[2])
    ui.label_Salario.setText(f'R$ {func[3]:.2f}')
    ui.label_HoraExtra.setText(str(func[4]))
    ui.label_PagExtra.setText(f'R$ {Valorhr(func[3],func[4]):.2f}')
def inserirHora():
    cpf = int(ui.label_CPF.text())
    hora = int(ui.lineEdit_HoraExtra.text())
    Doc.attHora(cpf, hora)
    buscar()

def Valorhr(salario, tempo):
    return (salario/180)*1.5*tempo

ui.pushButton_Buscar.clicked.connect(buscar)
ui.pushButton_InsereHE.clicked.connect(inserirHora)
app.exec_()