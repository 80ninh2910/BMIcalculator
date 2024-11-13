from ui.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalsAndSlots()

    def show(self):
        self.MainWindow.show()

    def setupSignalsAndSlots(self):
        pass


