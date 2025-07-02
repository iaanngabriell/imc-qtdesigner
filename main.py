import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interface_imc import Ui_MainWindow

class IMCApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.calcular_imc)
        self.ui.pushButton_2.clicked.connect(self.reset_formulario)

    def calcular_imc(self):
        try:
            peso = float(self.ui.lineEdit.text())
            altura = float(self.ui.lineEdit_2.text())

            imc = peso/(altura**2)

            classificacao = self.classificar_imc(imc)
            self.ui.label_result.setText(f"IMC:{imc:.2f} - {classificacao}")

        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira valores válidos para peso e altura.")

    def classificar_imc(self,imc):
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 25:
            return "Peso normal"
        elif 25 <= imc < 30:
            return "Sobrepeso"
        elif 30 <= imc < 35:
            return "Obesidade grau 1"
        elif 35 <= imc < 40:
            return "Obesidade grau 2"
        else:
            return "Obesidade grau 3 (mórbida)"
        
    def reset_formulario(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.label_result.clear()
        
app = QApplication(sys.argv)
janela = IMCApp()
janela.show()
sys.exit(app.exec_())