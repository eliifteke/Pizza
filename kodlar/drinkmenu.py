# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drinkmenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_drinkmenu(object):
    def d1(self, id):
        pizza = self.getPrice(id)
        print(str(pizza))
        n = int(self.textEdit_5.toPlainText())
        print(pizza, n)
        t = n * pizza
        self.label_43.setText('%0.2f' % t)

    def d2(self, id):
        pizza = self.getPrice(id)
        print(str(pizza))
        n = int(self.textEdit_6.toPlainText())
        print(pizza, n)
        t = n * pizza
        self.label_44.setText('%0.2f' % t)

    def d3(self, id):
        pizza = self.getPrice(id)
        print(str(pizza))
        n = int(self.textEdit_7.toPlainText())
        print(pizza, n)
        t = n * pizza
        self.label_45.setText('%0.2f' % t)

    def d4(self, id):
        pizza = self.getPrice(id)
        print(str(pizza))
        n = int(self.textEdit_8.toPlainText())
        print(pizza, n)
        t = n * pizza
        self.label_46.setText('%0.2f' % t)

    def d5(self, id):
        pizza = self.getPrice(id)
        print(str(pizza))
        n = int(self.textEdit_9.toPlainText())
        print(pizza, n)
        t = n * pizza
        self.label_47.setText('%0.2f' % t)

    def comp(self):

        total = 0
        if (self.checkBox_5.isChecked()):
            a = self.label_43.text()
            total += float(a)
            print(total)
            self.label_2.setText('%0.2f' % total)
        if (self.checkBox_6.isChecked()):
            b = self.label_44.text()
            total += float(b)
            print(total)
            self.label_2.setText('%0.2f' % total)

        if (self.checkBox_7.isChecked()):
            c = self.label_45.text()
            total += float(c)
            print(total)
            self.label_2.setText('%0.2f' % total)

        if (self.checkBox_8.isChecked()):
            d = self.label_46.text()
            total += float(d)
            print(total)
            self.label_2.setText('%0.2f' % total)

        if (self.checkBox_9.isChecked()):
            e = self.label_47.text()
            total += float(e)
            print(total)
            self.label_2.setText('%0.2f' % total)


    def setupUi(self, drinkmenu):
        drinkmenu.setObjectName("drinkmenu")
        drinkmenu.resize(803, 813)
        drinkmenu.setStyleSheet("#drinkmenu{\n"
"border-image: url(resim/drinkss.jpg);\n"
"}")
        self.pushButton_5 = QtWidgets.QPushButton(drinkmenu)
        self.pushButton_5.setGeometry(QtCore.QRect(590, 50, 131, 41))
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
        self.pushButton_12 = QtWidgets.QPushButton(drinkmenu)
        self.pushButton_12.setGeometry(QtCore.QRect(410, 700, 131, 41))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resim/cart.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setAutoDefault(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_11 = QtWidgets.QPushButton(drinkmenu)
        self.pushButton_11.setGeometry(QtCore.QRect(230, 700, 131, 41))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/more.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setAutoDefault(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.textEdit_8 = QtWidgets.QTextEdit(drinkmenu)
        self.textEdit_8.setGeometry(QtCore.QRect(570, 420, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_8.setFont(font)
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_7 = QtWidgets.QTextEdit(drinkmenu)
        self.textEdit_7.setGeometry(QtCore.QRect(570, 350, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_7.setFont(font)
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_6 = QtWidgets.QTextEdit(drinkmenu)
        self.textEdit_6.setGeometry(QtCore.QRect(570, 280, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_46 = QtWidgets.QLabel(drinkmenu)
        self.label_46.setGeometry(QtCore.QRect(670, 410, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"border-radius: 10px;\n"
"")
        self.label_46.setText("")
        self.label_46.setObjectName("label_46")
        self.label_2 = QtWidgets.QLabel(drinkmenu)
        self.label_2.setGeometry(QtCore.QRect(640, 590, 111, 51))
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
        self.label_19 = QtWidgets.QLabel(drinkmenu)
        self.label_19.setGeometry(QtCore.QRect(390, 270, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgb(43, 26, 19);\n"
"color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"color: rgb(246, 246, 246);\n"
"border-radius: 10px;\n"
"")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.pushButton = QtWidgets.QPushButton(drinkmenu)
        self.pushButton.setGeometry(QtCore.QRect(140, 130, 151, 41))
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
        self.pushButton_2 = QtWidgets.QPushButton(drinkmenu)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 130, 141, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);\n"
"border-radius: 10px;\n"
"\n"
"border-radius: 10px;\n"
"font: 20pt \"MV Boli\";")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resim/money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox_7 = QtWidgets.QCheckBox(drinkmenu)
        self.checkBox_7.setGeometry(QtCore.QRect(110, 340, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);")
        self.checkBox_7.setObjectName("checkBox_7")
        self.label_18 = QtWidgets.QLabel(drinkmenu)
        self.label_18.setGeometry(QtCore.QRect(390, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"color: rgb(246, 246, 246);\n"
"border-radius: 10px;\n"
"")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_21 = QtWidgets.QLabel(drinkmenu)
        self.label_21.setGeometry(QtCore.QRect(390, 420, 101, 41))
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
        self.label_43 = QtWidgets.QLabel(drinkmenu)
        self.label_43.setGeometry(QtCore.QRect(670, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"border-radius: 10px;\n"
"")
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.label_45 = QtWidgets.QLabel(drinkmenu)
        self.label_45.setGeometry(QtCore.QRect(670, 340, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"border-radius: 10px;\n"
"")
        self.label_45.setText("")
        self.label_45.setObjectName("label_45")
        self.checkBox_8 = QtWidgets.QCheckBox(drinkmenu)
        self.checkBox_8.setGeometry(QtCore.QRect(110, 420, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);")
        self.checkBox_8.setObjectName("checkBox_8")
        self.label_44 = QtWidgets.QLabel(drinkmenu)
        self.label_44.setGeometry(QtCore.QRect(670, 270, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"border-radius: 10px;\n"
"")
        self.label_44.setText("")
        self.label_44.setObjectName("label_44")
        self.pushButton_3 = QtWidgets.QPushButton(drinkmenu)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 130, 201, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);\n"
"border-radius: 10px;\n"
"\n"
"border-radius: 10px;\n"
"font: 20pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_18 = QtWidgets.QPushButton(drinkmenu)
        self.pushButton_18.setGeometry(QtCore.QRect(370, 590, 231, 51))
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
        self.pushButton_18.setIcon(icon3)
        self.pushButton_18.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_20 = QtWidgets.QLabel(drinkmenu)
        self.label_20.setGeometry(QtCore.QRect(390, 340, 101, 41))
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
        self.checkBox_6 = QtWidgets.QCheckBox(drinkmenu)
        self.checkBox_6.setGeometry(QtCore.QRect(110, 270, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);")
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_5 = QtWidgets.QCheckBox(drinkmenu)
        self.checkBox_5.setGeometry(QtCore.QRect(110, 200, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);")
        self.checkBox_5.setObjectName("checkBox_5")
        self.textEdit_5 = QtWidgets.QTextEdit(drinkmenu)
        self.textEdit_5.setGeometry(QtCore.QRect(570, 210, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setObjectName("textEdit_5")
        self.checkBox_9 = QtWidgets.QCheckBox(drinkmenu)
        self.checkBox_9.setGeometry(QtCore.QRect(110, 490, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);")
        self.checkBox_9.setObjectName("checkBox_9")
        self.textEdit_9 = QtWidgets.QTextEdit(drinkmenu)
        self.textEdit_9.setGeometry(QtCore.QRect(570, 490, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_9.setFont(font)
        self.textEdit_9.setObjectName("textEdit_9")
        self.label_47 = QtWidgets.QLabel(drinkmenu)
        self.label_47.setGeometry(QtCore.QRect(670, 480, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"border-radius: 10px;\n"
"")
        self.label_47.setText("")
        self.label_47.setObjectName("label_47")
        self.label_22 = QtWidgets.QLabel(drinkmenu)
        self.label_22.setGeometry(QtCore.QRect(390, 490, 101, 41))
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

        self.retranslateUi(drinkmenu)
        QtCore.QMetaObject.connectSlotsByName(drinkmenu)
        self.Form = drinkmenu
        self.checkBox_5.clicked.connect(lambda: self.d1(1))
        self.checkBox_6.clicked.connect(lambda: self.d2(2))
        self.checkBox_7.clicked.connect(lambda: self.d3(3))
        self.checkBox_8.clicked.connect(lambda: self.d4(4))
        self.checkBox_9.clicked.connect(lambda: self.d5(5))

        self.pushButton_5.clicked.connect(self.gitmusterigiris)
        self.pushButton_11.clicked.connect(self.gitmenu)
        self.pushButton_12.clicked.connect(self.gitsepet)

        self.pushButton_18.clicked.connect(self.comp)

        self.checkBox_5.clicked.connect(lambda: self.buyrun(drinkmenu))
        self.checkBox_6.clicked.connect(lambda: self.buyrunn(drinkmenu))
        self.checkBox_7.clicked.connect(lambda: self.buyrunnn(drinkmenu))
        self.checkBox_8.clicked.connect(lambda: self.buyrunnnn(drinkmenu))
        self.checkBox_9.clicked.connect(lambda: self.buyrunnnnn(drinkmenu))

    def buyrun(self,drinkmenu):
        if (self.checkBox_5.isChecked()):
            name = self.checkBox_5.text()

            quantity = self.textEdit_5.toPlainText()

            price = self.label_43.text()

            conn = sqlite3.connect('pizza.db')
            query = "INSERT INTO cart (name, quantity, price) VALUES ('%s','%s','%s')" % (name, quantity, price)
            print(query)
            conn.execute(query)
            conn.commit()
            conn.close()

    def buyrunn(self,drinkmenu):
        if (self.checkBox_6.isChecked()):
            name = self.checkBox_6.text()

            quantity = self.textEdit_6.toPlainText()

            price = self.label_44.text()

            conn = sqlite3.connect('pizza.db')
            query = "INSERT INTO cart (name, quantity, price) VALUES ('%s','%s','%s')" % (name, quantity, price)
            print(query)
            conn.execute(query)
            conn.commit()
            conn.close()


    def buyrunnn(self,drinkmenu):
        if (self.checkBox_7.isChecked()):
            name = self.checkBox_7.text()

            quantity = self.textEdit_7.toPlainText()

            price = self.label_45.text()

            conn = sqlite3.connect('pizza.db')
            query = "INSERT INTO cart (name, quantity, price) VALUES ('%s','%s','%s')" % (name, quantity, price)
            print(query)
            conn.execute(query)
            conn.commit()
            conn.close()

    def buyrunnnn(self,drinkmenu):
        if (self.checkBox_8.isChecked()):
            name = self.checkBox_8.text()

            quantity = self.textEdit_8.toPlainText()

            price = self.label_46.text()

            conn = sqlite3.connect('pizza.db')
            query = "INSERT INTO cart (name, quantity, price) VALUES ('%s','%s','%s')" % (name, quantity, price)
            print(query)
            conn.execute(query)
            conn.commit()
            conn.close()

    def buyrunnnnn(self,drinkmenu):
        if (self.checkBox_9.isChecked()):
            name = self.checkBox_9.text()

            quantity = self.textEdit_9.toPlainText()

            price = self.label_47.text()

            conn = sqlite3.connect('pizza.db')
            query = "INSERT INTO cart (name, quantity, price) VALUES ('%s','%s','%s')" % (name, quantity, price)
            print(query)
            conn.execute(query)
            conn.commit()
            conn.close()



    def retranslateUi(self, drinkmenu):
        _translate = QtCore.QCoreApplication.translate
        drinkmenu.setWindowTitle(_translate("drinkmenu", "Form"))
        self.pushButton_5.setText(_translate("drinkmenu", "LOGOUT"))
        self.pushButton_12.setText(_translate("drinkmenu", "CART"))
        self.pushButton_11.setText(_translate("drinkmenu", "ADD MORE"))
        self.pushButton.setText(_translate("drinkmenu", "KIND"))
        self.pushButton_2.setText(_translate("drinkmenu", "COST"))
        self.checkBox_7.setText(_translate("drinkmenu", "SPRITE"))
        self.checkBox_8.setText(_translate("drinkmenu", "FRUIT JUICE"))
        self.pushButton_3.setText(_translate("drinkmenu", "QUANTITY"))
        self.pushButton_18.setText(_translate("drinkmenu", "Total Cost"))
        self.checkBox_6.setText(_translate("drinkmenu", "FANTA"))
        self.checkBox_5.setText(_translate("drinkmenu", "COLA"))
        self.checkBox_9.setText(_translate("drinkmenu", "LEMONADE"))
        self.label_18.setText(_translate("drinkmenu", "10.00"))
        self.label_19.setText(_translate("drinkmenu", "10.00"))
        self.label_20.setText(_translate("drinkmenu", "10.00"))
        self.label_21.setText(_translate("drinkmenu", "10.00"))
        self.label_22.setText(_translate("drinkmenu", "10.00"))



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
        content = 'select cost from drink where drinkID= %d' % id
        res = curs.execute(content)
        for data in res:
            return int(data[0])

from resim import YeniMetinBelgesi_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    drinkmenu = QtWidgets.QWidget()
    ui = Ui_drinkmenu()
    ui.setupUi(drinkmenu)
    drinkmenu.show()
    sys.exit(app.exec_())
