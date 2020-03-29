# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminmenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminmenu(object):
    def setupUi(self, adminmenu):
        adminmenu.setObjectName("adminmenu")
        adminmenu.resize(752, 403)
        adminmenu.setStyleSheet("#adminmenu{\n"
"border-image: url(:/newPrefix/piza.jpg);\n"
"}")
        self.pushButton = QtWidgets.QPushButton(adminmenu)
        self.pushButton.setGeometry(QtCore.QRect(410, 260, 191, 71))
        self.pushButton.setStyleSheet(".QPushButton{\n"
"font: 20pt \"Ink Free\";\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(35, 35))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(adminmenu)
        QtCore.QMetaObject.connectSlotsByName(adminmenu)

        self.Form = adminmenu
        self.pushButton.clicked.connect(self.gitnewadmin)

    def retranslateUi(self, adminmenu):
        _translate = QtCore.QCoreApplication.translate
        adminmenu.setWindowTitle(_translate("adminmenu", "Form"))
        self.pushButton.setText(_translate("adminmenu", "ADMINS"))
        self.pushButton.setShortcut(_translate("adminmenu", "5"))


    def gitnewadmin(self):
        from newadmin import Ui_newadmin
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_newadmin()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için
from resim import YeniMetinBelgesi_rc





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminmenu = QtWidgets.QWidget()
    ui = Ui_adminmenu()
    ui.setupUi(adminmenu)
    adminmenu.show()
    sys.exit(app.exec_())
