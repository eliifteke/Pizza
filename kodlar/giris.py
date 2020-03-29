# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giris.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_giris(object):
    def setupUi(self, giris):
        self.Form = giris
        giris.setObjectName("giris")
        giris.resize(810, 468)
        giris.setStyleSheet("#giris{ \n"
"background-image: url(:/newPrefix/pizza.jpg)\n"
"}\n"
"\n"
"")
        self.pushButton = QtWidgets.QPushButton(giris)
        self.pushButton.setGeometry(QtCore.QRect(50, 190, 701, 101))
        self.pushButton.setStyleSheet(".QPushButton{\n"
"font: 30pt \"Ink Free\";\n"
"border-radius: 30px;\n"
"background: rgb(170, 170, 255);\n"
"}\n"
"\n"
"\n"
".QPushButton:hover\n"
"{\n"
" \n"
"    background-color: rgb(100, 100, 255);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(giris)
        QtCore.QMetaObject.connectSlotsByName(giris)
        self.pushButton.clicked.connect(self.gitmusterigiris)
    def retranslateUi(self, giris):
        _translate = QtCore.QCoreApplication.translate
        giris.setWindowTitle(_translate("giris", "Form"))
        self.pushButton.setText(_translate("giris", " Click Here and Come To Pizza"))

    def gitmusterigiris(self):
        from musterigiris import Ui_musterigiris
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_musterigiris()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()   #önceki sayfayı kapatmak için

from resim import YeniMetinBelgesi_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    giris = QtWidgets.QWidget()
    ui = Ui_giris()
    ui.setupUi(giris)
    giris.show()
    sys.exit(app.exec_())
