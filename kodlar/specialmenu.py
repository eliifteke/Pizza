# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'specialmenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_specialmenu(object):
    def s1(self, id):
        pizza = self.getPrice(id)
        print(str(pizza))
        n = int(self.textEdit_10.toPlainText())
        print(pizza, n)
        t = n * pizza
        self.label_48.setText('%0.2f' % t)

    def s2(self, id):
        pizza = self.getPrice(id)
        print(str(pizza))
        n = int(self.textEdit_11.toPlainText())
        print(pizza, n)
        t = n * pizza
        self.label_49.setText('%0.2f' % t)

    def s3(self, id):
        pizza = self.getPrice(id)
        print(str(pizza))
        n = int(self.textEdit_12.toPlainText())
        print(pizza, n)
        t = n * pizza
        self.label_50.setText('%0.2f' % t)


    def comp(self):

        total = 0
        if (self.checkBox_10.isChecked()):
            a = self.label_48.text()
            total += float(a)
            print(total)
            self.label_2.setText('%0.2f' % total)

        if (self.checkBox_11.isChecked()):
            b = self.label_49.text()
            total += float(b)
            print(total)
            self.label_2.setText('%0.2f' % total)

        if (self.checkBox_12.isChecked()):
            c = self.label_50.text()
            total += float(c)
            print(total)
            self.label_2.setText('%0.2f' % total)



    def setupUi(self, specialmenu):
        specialmenu.setObjectName("specialmenu")
        specialmenu.resize(1133, 635)
        specialmenu.setStyleSheet("#specialmenu{\n"
"\n"
"    border-image: url(resim/speciall.jpg);\n"
"}")
        self.pushButton_11 = QtWidgets.QPushButton(specialmenu)
        self.pushButton_11.setGeometry(QtCore.QRect(230, 550, 131, 41))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(".QPushButton\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/more.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setAutoDefault(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_5 = QtWidgets.QPushButton(specialmenu)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 30, 131, 41))
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
        self.pushButton_12 = QtWidgets.QPushButton(specialmenu)
        self.pushButton_12.setGeometry(QtCore.QRect(390, 560, 131, 41))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet(".QPushButton\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resim/cart.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon1)
        self.pushButton_12.setAutoDefault(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_2 = QtWidgets.QLabel(specialmenu)
        self.label_2.setGeometry(QtCore.QRect(480, 450, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(246, 246, 246);\n"
"background-color: rgb(0, 85, 127);\n"
"border-radius: 10px\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.textEdit_12 = QtWidgets.QTextEdit(specialmenu)
        self.textEdit_12.setGeometry(QtCore.QRect(500, 360, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_12.setFont(font)
        self.textEdit_12.setObjectName("textEdit_12")
        self.checkBox_12 = QtWidgets.QCheckBox(specialmenu)
        self.checkBox_12.setGeometry(QtCore.QRect(40, 360, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);")
        self.checkBox_12.setObjectName("checkBox_12")
        self.label_21 = QtWidgets.QLabel(specialmenu)
        self.label_21.setGeometry(QtCore.QRect(320, 290, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgb(43, 26, 19);\n"
"color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"color: rgb(246, 246, 246);\n"
"border-radius: 10px;\n"
"\n"
"")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.pushButton = QtWidgets.QPushButton(specialmenu)
        self.pushButton.setGeometry(QtCore.QRect(70, 120, 151, 41))
        self.pushButton.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);\n"
"\n"
"border-radius: 10px;\n"
"font: 20pt \"MV Boli\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/p.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.label_50 = QtWidgets.QLabel(specialmenu)
        self.label_50.setGeometry(QtCore.QRect(600, 350, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"border-radius: 10px;\n"
"")
        self.label_50.setText("")
        self.label_50.setObjectName("label_50")
        self.label_48 = QtWidgets.QLabel(specialmenu)
        self.label_48.setGeometry(QtCore.QRect(600, 210, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"border-radius: 10px;\n"
"")
        self.label_48.setText("")
        self.label_48.setObjectName("label_48")
        self.pushButton_18 = QtWidgets.QPushButton(specialmenu)
        self.pushButton_18.setGeometry(QtCore.QRect(210, 450, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet(".QPushButton{\n"
"color: rgb(246, 246, 246);\n"
"background-color: rgb(0, 85, 127);\n"
"border-radius: 10px;\n"
"\n"
"}\n"
".QPushButton:hover\n"
"{\n"
"     background-color: rgb(0, 150, 127);\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resim/money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_18.setIcon(icon3)
        self.pushButton_18.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_18.setObjectName("pushButton_18")
        self.checkBox_11 = QtWidgets.QCheckBox(specialmenu)
        self.checkBox_11.setGeometry(QtCore.QRect(40, 290, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);")
        self.checkBox_11.setObjectName("checkBox_11")
        self.textEdit_11 = QtWidgets.QTextEdit(specialmenu)
        self.textEdit_11.setGeometry(QtCore.QRect(500, 290, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_11.setFont(font)
        self.textEdit_11.setObjectName("textEdit_11")
        self.label_49 = QtWidgets.QLabel(specialmenu)
        self.label_49.setGeometry(QtCore.QRect(600, 280, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"border-radius: 10px;\n"
"")
        self.label_49.setText("")
        self.label_49.setObjectName("label_49")
        self.pushButton_3 = QtWidgets.QPushButton(specialmenu)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 120, 201, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);\n"
"border-radius: 10px;\n"
"\n"
"border-radius: 10px;\n"
"font: 20pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_22 = QtWidgets.QLabel(specialmenu)
        self.label_22.setGeometry(QtCore.QRect(320, 360, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color: rgb(43, 26, 19);\n"
"color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"color: rgb(246, 246, 246);\n"
"border-radius: 10px;\n"
"\n"
"")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.textEdit_10 = QtWidgets.QTextEdit(specialmenu)
        self.textEdit_10.setGeometry(QtCore.QRect(500, 220, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_10.setFont(font)
        self.textEdit_10.setObjectName("textEdit_10")
        self.pushButton_2 = QtWidgets.QPushButton(specialmenu)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 120, 141, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);\n"
"border-radius: 10px;\n"
"\n"
"border-radius: 10px;\n"
"font: 20pt \"MV Boli\";")
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_20 = QtWidgets.QLabel(specialmenu)
        self.label_20.setGeometry(QtCore.QRect(320, 210, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgb(43, 26, 19);\n"
"color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"color: rgb(246, 246, 246);\n"
"border-radius: 10px;\n"
"\n"
"")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.checkBox_10 = QtWidgets.QCheckBox(specialmenu)
        self.checkBox_10.setGeometry(QtCore.QRect(40, 210, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);")
        self.checkBox_10.setObjectName("checkBox_10")

        self.retranslateUi(specialmenu)
        QtCore.QMetaObject.connectSlotsByName(specialmenu)

        self.Form = specialmenu
        self.checkBox_10.clicked.connect(lambda: self.s1(1))
        self.checkBox_11.clicked.connect(lambda: self.s2(2))
        self.checkBox_12.clicked.connect(lambda: self.s3(3))

        self.pushButton_5.clicked.connect(self.gitmusterigiris)
        self.pushButton_11.clicked.connect(self.gitmenu)
        self.pushButton_12.clicked.connect(self.gitsepet)
        self.pushButton_18.clicked.connect(self.comp)

        self.checkBox_10.clicked.connect(lambda: self.buyrun(specialmenu))
        self.checkBox_11.clicked.connect(lambda: self.buyrunn(specialmenu))
        self.checkBox_12.clicked.connect(lambda: self.buyrunnn(specialmenu))


    def buyrun(self,specialmenu):
        if (self.checkBox_10.isChecked()):
            name = self.checkBox_10.text()

            quantity = self.textEdit_10.toPlainText()

            price = self.label_48.text()

            conn = sqlite3.connect('pizza.db')
            query = "INSERT INTO cart (name, quantity, price) VALUES ('%s','%s','%s')" % (name, quantity, price)
            print(query)
            conn.execute(query)
            conn.commit()
            conn.close()

    def buyrunn(self,specialmenu):
        if (self.checkBox_11.isChecked()):
            name = self.checkBox_11.text()

            quantity = self.textEdit_11.toPlainText()

            price = self.label_49.text()

            conn = sqlite3.connect('pizza.db')
            query = "INSERT INTO cart (name, quantity, price) VALUES ('%s','%s','%s')" % (name, quantity, price)
            print(query)
            conn.execute(query)
            conn.commit()
            conn.close()


    def buyrunnn(self,specialmenu):
        if (self.checkBox_12.isChecked()):
            name = self.checkBox_12.text()

            quantity = self.textEdit_12.toPlainText()

            price = self.label_50.text()

            conn = sqlite3.connect('pizza.db')
            query = "INSERT INTO cart (name, quantity, price) VALUES ('%s','%s','%s')" % (name, quantity, price)
            print(query)
            conn.execute(query)
            conn.commit()
            conn.close()

    def retranslateUi(self, specialmenu):
        _translate = QtCore.QCoreApplication.translate
        specialmenu.setWindowTitle(_translate("specialmenu", "Form"))
        self.pushButton_11.setText(_translate("specialmenu", "ADD MORE"))
        self.pushButton_5.setText(_translate("specialmenu", "LOGOUT"))
        self.pushButton_12.setText(_translate("specialmenu", "CART"))
        self.checkBox_12.setText(_translate("specialmenu", "SUFLE"))
        self.pushButton.setText(_translate("specialmenu", "KIND"))
        self.pushButton_18.setText(_translate("specialmenu", "Total Cost"))
        self.checkBox_11.setText(_translate("specialmenu", "FRIED POTATOES"))
        self.pushButton_3.setText(_translate("specialmenu", "QUANTITY"))
        self.pushButton_2.setText(_translate("specialmenu", "COST"))
        self.checkBox_10.setText(_translate("specialmenu", "HAMBURGER"))

        self.label_20.setText(_translate("specialmenu", "30.00"))
        self.label_21.setText(_translate("specialmenu", "15.00"))
        self.label_22.setText(_translate("specialmenu", "20.00"))

    def gitmusterigiris(self):
        from musterigiris import Ui_musterigiris
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_musterigiris()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için

    def gitmenu(self):
        from menu import Ui_menu
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_menu()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için

    def gitsepet(self):
        from sepet import Ui_sepet
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_sepet()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için

    def getPrice(self, id):
        conn = sqlite3.connect('pizza.db')
        curs = conn.cursor()
        content = 'select cost from special where specialID= %d' % id
        res = curs.execute(content)
        for data in res:
            return int(data[0])



from resim import YeniMetinBelgesi_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    specialmenu = QtWidgets.QWidget()
    ui = Ui_specialmenu()
    ui.setupUi(specialmenu)
    specialmenu.show()
    sys.exit(app.exec_())
