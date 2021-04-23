import sys
from ui.payment_ui import Ui_MainWindow
from entity.company import calculate_salary

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog


class UI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle("Pagamento")
        self.btnCalculateSalary.clicked.connect(self.calculate_salary)
    
    def value_salary(self):
        msg = QMessageBox()
        try:
            salary = float(self.lineSalary.text())
            days_to_work = float(self.lineDaysToWork.text())
            worked_days = float(self.lineWorkedDays.text())
            justified_absences = float(self.lineJustifiedAbsences.text())
            if worked_days + justified_absences > days_to_work:
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Valor Informado inválido")
                msg.setInformativeText(
                    "Os dias previsto para trabalhar não podem ser inferior a soma dos dias trabalhados com as faltas justificadas")
                msg.setWindowTitle("Dia Previsto Para Trabalhar")
                msg.exec_()
                self.btnGeneratorPDF.setEnabled(False)
            else:
                salary = calculate_salary(salary, days_to_work, worked_days, justified_absences)
                salary = round(salary, 2)
                self.linePayment.setText(str(salary))

        except:
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Valor Informado inválido")
            msg.setInformativeText("Verifique os campos digitados, um ou mais campos foram digitados incorretamente "
                                   "ou estão vazios")
            msg.setWindowTitle("Campo Inválido")
            msg.exec_()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    ui = UI()
    ui.show()
    qt.exec_()
