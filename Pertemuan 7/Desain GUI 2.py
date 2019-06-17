# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desain_GUI_2.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(519, 326)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 70, 211, 16))
        self.label.setObjectName("label")
        self.ButtonHallo = QtWidgets.QPushButton(Form)
        self.ButtonHallo.setGeometry(QtCore.QRect(170, 160, 75, 23))
        self.ButtonHallo.setObjectName("ButtonHallo")
        self.ButtonClear = QtWidgets.QPushButton(Form)
        self.ButtonClear.setGeometry(QtCore.QRect(260, 160, 75, 23))
        self.ButtonClear.setObjectName("ButtonClear")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 210, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.NamaEdit = QtWidgets.QLineEdit(Form)
        self.NamaEdit.setGeometry(QtCore.QRect(140, 110, 241, 21))
        self.NamaEdit.setObjectName("NamaEdit")

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(Form.close)
        self.ButtonClear.clicked.connect(self.NamaEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Masukan Nama Anda :</span></p></body></html>"))
        self.ButtonHallo.setText(_translate("Form", "Hallo"))
        self.ButtonClear.setText(_translate("Form", "Clear"))
        self.pushButton_3.setText(_translate("Form", "Exit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
