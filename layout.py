# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(744, 457)
        Dialog.setStyleSheet("color: {\"#F5DDDD\"}")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 30, 345, 200))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.imie = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.imie.setObjectName("imie")
        self.horizontalLayout.addWidget(self.imie)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.wiek = QtWidgets.QSpinBox(parent=self.verticalLayoutWidget)
        self.wiek.setMaximum(30)
        self.wiek.setObjectName("wiek")
        self.horizontalLayout_2.addWidget(self.wiek)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.rodzajzwierzat = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.rodzajzwierzat.setObjectName("rodzajzwierzat")
        self.rodzajzwierzat.addItem("")
        self.rodzajzwierzat.addItem("")
        self.rodzajzwierzat.addItem("")
        self.verticalLayout.addWidget(self.rodzajzwierzat)
        self.lekarze = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.lekarze.setObjectName("lekarze")
        self.lekarze.addItem("")
        self.lekarze.setItemText(0, "")
        self.verticalLayout.addWidget(self.lekarze)
        self.wizytapilna = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.wizytapilna.setChecked(True)
        self.wizytapilna.setObjectName("wizytapilna")
        self.verticalLayout.addWidget(self.wizytapilna)
        self.zarejestruj = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.zarejestruj.setObjectName("zarejestruj")
        self.verticalLayout.addWidget(self.zarejestruj)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Zarejestruj swojego pupila na wizytę"))
        self.label_2.setText(_translate("Dialog", "Imie"))
        self.label_3.setText(_translate("Dialog", "Wiek"))
        self.rodzajzwierzat.setItemText(0, _translate("Dialog", "pies"))
        self.rodzajzwierzat.setItemText(1, _translate("Dialog", "kot"))
        self.rodzajzwierzat.setItemText(2, _translate("Dialog", "chomik"))
        self.wizytapilna.setText(_translate("Dialog", "wizyta pilna"))
        self.zarejestruj.setText(_translate("Dialog", "Zarejestruj"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
