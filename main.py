import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class SecondWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('potwierdzenie wizyty')
        self.show()


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Wet Plus - twoja przychodnia weterynaryjna")
        self.ui.label.setStyleSheet("color: #6B4E71")
        self.ui.label_2.setStyleSheet("color: #3A4454")
        self.ui.label_3.setStyleSheet("color: #3A4454")
        self.ui.zarejestruj.clicked.connect(self.zarejestruj)
        self.ui.zarejestruj.setStyleSheet("background-color: #C2B2B4")
        with open('lekarze.txt', 'r') as lekarze:
            for line in lekarze:
                self.ui.lekarze.addItem(line)
            lekarze.close()
        self.show()

    def zarejestruj(self):
        app2 = QApplication(sys.argv)
        ex2 = SecondWindow()
        ex2.show()
        app2.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    ex.show()
    app.exec()
