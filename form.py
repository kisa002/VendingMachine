# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.btnOrder = QtWidgets.QPushButton(Dialog)
        self.btnOrder.setGeometry(QtCore.QRect(10, 110, 113, 32))
        self.btnOrder.setObjectName("btnOrder")
        self.lblCount = QtWidgets.QLabel(Dialog)
        self.lblCount.setGeometry(QtCore.QRect(30, 50, 71, 16))
        self.lblCount.setObjectName("lblCount")

        self.retranslateUi(Dialog)
        self.btnOrder.clicked.connect(Dialog.Order)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnOrder.setText(_translate("Dialog", "Order"))
        self.lblCount.setText(_translate("Dialog", "Count: 10"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
