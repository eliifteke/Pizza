# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu(object):
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(699, 814)
        menu.setStyleSheet("#menu{\n"
"border-image: url(resim/menu.jpg);\n"
"}")
        self.pushButton_5 = QtWidgets.QPushButton(menu)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(".QPushButton\n"
"{\n"
"background: rgb(170,170, 255);\n"
"\n"
"font: 18pt \"8514oem\";\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton:hover\n"
"{\n"
"     background-color: rgb(100, 150, 255);\n"
"}\n"
"")
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(menu)
        self.pushButton_6.setGeometry(QtCore.QRect(110, 220, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(".QPushButton\n"
"{\n"
"background: rgb(170,170, 255);\n"
"\n"
"font: 30pt \"Ink Free\";\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton:hover\n"
"{\n"
"     background-color: rgb(100, 150, 255);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/p.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(menu)
        self.pushButton_7.setGeometry(QtCore.QRect(110, 310, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(".QPushButton\n"
"{\n"
"background: rgb(170,170, 255);\n"
"\n"
"font: 30pt \"Ink Free\";\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton:hover\n"
"{\n"
"     background-color: rgb(100, 150, 255);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resim/drink.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(menu)
        self.pushButton_8.setGeometry(QtCore.QRect(110, 400, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(".QPushButton\n"
"{\n"
"background: rgb(170,170, 255);\n"
"\n"
"font: 30pt \"Ink Free\";\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton:hover\n"
"{\n"
"     background-color: rgb(100, 150, 255);\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resim/specialmenu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(menu)
        self.pushButton_9.setGeometry(QtCore.QRect(110, 500, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(".QPushButton\n"
"{\n"
"background: rgb(170,170, 255);\n"
"\n"
"font: 30pt \"Ink Free\";\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton:hover\n"
"{\n"
"     background-color: rgb(100, 150, 255);\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resim/alllist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon3)
        self.pushButton_9.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_9.setAutoDefault(False)
        self.pushButton_9.setObjectName("pushButton_9")

        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)

        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)
        self.Form = menu
        self.pushButton_5.clicked.connect(self.gitmusterigiris)
        self.pushButton_6.clicked.connect(self.gitpizzamenu)
        self.pushButton_7.clicked.connect(self.gitdrinkmenu)
        self.pushButton_8.clicked.connect(self.gitspecialmenu)
        self.pushButton_9.clicked.connect(self.gitlistmenu)

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "Form"))
        self.pushButton_5.setText(_translate("menu", "LOGOUT"))
        self.pushButton_6.setText(_translate("menu", "PIZZA\'S MENU"))
        self.pushButton_7.setText(_translate("menu", "DRINK\'S MENU"))
        self.pushButton_7.setShortcut(_translate("menu", "Enter"))
        self.pushButton_8.setText(_translate("menu", "SPECIAL\'S MENU"))
        self.pushButton_9.setText(_translate("menu", "ALL MENU LIST"))

    def gitmusterigiris(self):
        from musterigiris import Ui_musterigiris
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_musterigiris()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için

    def gitpizzamenu(self):
        from pizzamenu import Ui_pizzamenu
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_pizzamenu()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için

    def gitdrinkmenu(self):
        from drinkmenu import Ui_drinkmenu
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_drinkmenu()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için

    def gitspecialmenu(self):
        from specialmenu import Ui_specialmenu
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_specialmenu()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için

    def gitlistmenu(self):
        from listmenu import Ui_listmenu
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_listmenu()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için


from resim import YeniMetinBelgesi_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu = QtWidgets.QWidget()
    ui = Ui_menu()
    ui.setupUi(menu)
    menu.show()
    sys.exit(app.exec_())
