from BMI_Lib import CalBMI
from ui.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalsAndSlots()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalsAndSlots(self):
        self.pushButtoncal.clicked.connect(self.Cal)
    def Cal(self):
        height=float(self.lineEditheight.text())
        weight=float(self.lineEditweight.text())
        bmi=CalBMI(height,weight)

