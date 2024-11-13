from BMI_Lib import Status, BMI
from ui.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalsAndSlots()
        self.pushButtonRe.clicked.connect(self.process_clear)



    def setupSignalsAndSlots(self):
        self.pushButtoncal.clicked.connect(self.Cal)

    def Cal(self):
        height=float(self.lineEditheight.text())
        weight=float(self.lineEditweight.text())
        status=Status(height,weight)
        bmi=BMI(height,weight)
        self.lineEditBMI.setText(f"{bmi}")
        self.lineEditStatus.setText(f"{status}")

    def process_clear(self):
        self.lineEditweight.setText("")
        self.lineEditheight.setText("")
        self.lineEditStatus.setText("")
        self.lineEditBMI.setText("")
        self.lineEditweight.setFocus()

    def show(self):
        self.MainWindow.show()

