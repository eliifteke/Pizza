# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musterigiris.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_musterigiris(object):
    def setupUi(self, musterigiris):
        musterigiris.setObjectName("musterigiris")
        musterigiris.resize(861, 414)
        font = QtGui.QFont()
        font.setPointSize(19)
        musterigiris.setFont(font)
        musterigiris.setStyleSheet("#musterigiris{\n"
"\n"
"border-image: url(:/newPrefix/pizzaa.png);\n"
"}")
        self.formWidget = QtWidgets.QWidget(musterigiris)
        self.formWidget.setGeometry(QtCore.QRect(450, 130, 381, 151))
        self.formWidget.setStyleSheet("#formWidget{\n"
"\n"
"    background-color: rgb(62, 134, 200);\n"
"\n"
"border-radius: 15px\n"
"}")
        self.formWidget.setObjectName("formWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout.setContentsMargins(25, 40, 25, 15)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(musterigiris)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 300, 131, 41))
        self.pushButton_2.setStyleSheet(".QPushButton\n"
"{\n"
"background: rgb(170,170, 255);\n"
"\n"
"font: 15pt \"8514oem\";\n"
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
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(musterigiris)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 300, 161, 41))
        self.pushButton_3.setStyleSheet(".QPushButton\n"
"{\n"
"background: rgb(170,170, 255);\n"
"\n"
"font: 15pt \"8514oem\";\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton:hover\n"
"{\n"
"     background-color: rgb(100, 150, 255);\n"
"}\n"
"")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(musterigiris)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(".QPushButton\n"
"{\n"
"background: rgb(170,170, 255);\n"
"\n"
"font: 17pt \"8514oem\";\n"
"border-radius: 10px;\n"
"}\n"
"\n"
".QPushButton:hover\n"
"{\n"
"     background-color: rgb(100, 150, 255);\n"
"}\n"
"")
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(musterigiris)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 30, 131, 41))
        self.pushButton_5.setStyleSheet(".QPushButton\n"
"{\n"
"background: rgb(170,170, 255);\n"
"\n"
"font: 15pt \"8514oem\";\n"
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

        self.retranslateUi(musterigiris)
        QtCore.QMetaObject.connectSlotsByName(musterigiris)
        self.Form = musterigiris
        self.pushButton_3.clicked.connect(self.gitadminmenu)
        self.pushButton_2.clicked.connect(self.gitmenu)
        self.pushButton_4.clicked.connect(self.gitgiris)
        self.pushButton_5.clicked.connect(self.gitabout)


    def retranslateUi(self, musterigiris):
        _translate = QtCore.QCoreApplication.translate
        musterigiris.setWindowTitle(_translate("musterigiris", "Form"))
        self.label.setText(_translate("musterigiris", "Username :"))
        self.label_2.setText(_translate("musterigiris", "Password :"))
        self.pushButton_2.setText(_translate("musterigiris", "LOGIN"))
        self.pushButton_3.setText(_translate("musterigiris", "NEW MEMBER"))
        self.pushButton_4.setText(_translate("musterigiris", "HOME"))
        self.pushButton_5.setText(_translate("musterigiris", "ABOUT"))

    def gitadminmenu(self):
        from adminmenu import Ui_adminmenu
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_adminmenu()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için

    def gitmenu(self):
        import veribaglan
        username = self.lineEdit.text()
        password =self.lineEdit_2.text()

        veri = veribaglan.getLogin(username,password)

        if not veri:
            return ;

        from menu import Ui_menu
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_menu()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için

    def gitgiris(self):
        from giris import Ui_giris
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_giris()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için


    def gitabout(self):
        from about import Ui_about
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_about()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için

from resim import YeniMetinBelgesi_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    musterigiris = QtWidgets.QWidget()
    ui = Ui_musterigiris()
    ui.setupUi(musterigiris)
    musterigiris.show()
    sys.exit(app.exec_())
