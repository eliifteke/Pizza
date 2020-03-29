import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pizzamenu(object):




    def k1(self,id):
        pizza = self.getPrice(id)
        print (str(pizza))
        n = int(self.textEdit.toPlainText())
        print (pizza,n)
        t = n * pizza
        self.label_42.setText('%0.2f' % t)

    def k2(self,id):
        pizza = self.getPrice(id)
        print (str(pizza))
        n = int(self.textEdit_2.toPlainText())
        print (pizza,n)
        t = n * pizza
        self.label_41.setText('%0.2f' % t)

    def k3(self, id):
        pizza = self.getPrice(id)
        print (str(pizza))
        n = int(self.textEdit_3.toPlainText())
        print (pizza, n)
        t = n * pizza
        self.label_40.setText('%0.2f' % t)

    def k4(self, id):
            pizza = self.getPrice(id)
            print (str(pizza))
            n = int(self.textEdit_4.toPlainText())
            print (pizza, n)
            t = n * pizza
            self.label_39.setText('%0.2f' % t)



    def comp(self):

        total = 0
        if(self.checkBox.isChecked()):



           a = self.label_42.text()
           total += float(a)
           print (total)
           self.label_2.setText('%0.2f' % total)



        if( self.checkBox_2.isChecked()):
           b = self.label_41.text()
           total += float(b)
           print (total)
           self.label_2.setText('%0.2f' % total)

        if(self.checkBox_3.isChecked()):
           c = self.label_40.text()
           total += float(c)
           print (total)
           self.label_2.setText('%0.2f' % total)

        if (self.checkBox_4.isChecked()):
            d = self.label_39.text()
            total += float(d)
            print (total)
            self.label_2.setText('%0.2f' % total)




    def setupUi(self, pizzamenu):




        pizzamenu.setObjectName("pizzamenu")
        pizzamenu.resize(1099, 634)
        pizzamenu.setStyleSheet("#pizzamenu{\n"
"border-image: url(:/newPrefix/piza.png);\n"
"}")
        self.pushButton_5 = QtWidgets.QPushButton(pizzamenu)
        self.pushButton_5.setGeometry(QtCore.QRect(800, 30, 131, 41))
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
        self.pushButton_11 = QtWidgets.QPushButton(pizzamenu)
        self.pushButton_11.setGeometry(QtCore.QRect(910, 260, 131, 41))
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
        self.pushButton_12 = QtWidgets.QPushButton(pizzamenu)
        self.pushButton_12.setGeometry(QtCore.QRect(910, 330, 131, 41))
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
        self.label_21 = QtWidgets.QLabel(pizzamenu)
        self.label_21.setGeometry(QtCore.QRect(440, 420, 101, 41))
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
        self.label_19 = QtWidgets.QLabel(pizzamenu)
        self.label_19.setGeometry(QtCore.QRect(440, 270, 101, 41))
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
        self.label_20 = QtWidgets.QLabel(pizzamenu)
        self.label_20.setGeometry(QtCore.QRect(440, 340, 101, 41))
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
        self.label_18 = QtWidgets.QLabel(pizzamenu)
        self.label_18.setGeometry(QtCore.QRect(440, 200, 101, 41))
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
        self.checkBox_3 = QtWidgets.QCheckBox(pizzamenu)
        self.checkBox_3.setGeometry(QtCore.QRect(160, 340, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox = QtWidgets.QCheckBox(pizzamenu)
        self.checkBox.setGeometry(QtCore.QRect(160, 200, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(pizzamenu)
        self.checkBox_2.setGeometry(QtCore.QRect(160, 270, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_4 = QtWidgets.QCheckBox(pizzamenu)
        self.checkBox_4.setGeometry(QtCore.QRect(160, 420, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);")
        self.checkBox_4.setObjectName("checkBox_4")
        self.textEdit = QtWidgets.QTextEdit(pizzamenu)
        self.textEdit.setGeometry(QtCore.QRect(620, 210, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_4 = QtWidgets.QTextEdit(pizzamenu)
        self.textEdit_4.setGeometry(QtCore.QRect(620, 420, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_3 = QtWidgets.QTextEdit(pizzamenu)
        self.textEdit_3.setGeometry(QtCore.QRect(620, 350, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_2 = QtWidgets.QLabel(pizzamenu)
        self.label_2.setGeometry(QtCore.QRect(630, 520, 111, 51))
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
        self.textEdit_2 = QtWidgets.QTextEdit(pizzamenu)
        self.textEdit_2.setGeometry(QtCore.QRect(620, 280, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_18 = QtWidgets.QPushButton(pizzamenu)
        self.pushButton_18.setGeometry(QtCore.QRect(360, 520, 231, 51))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resim/money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_18.setIcon(icon2)
        self.pushButton_18.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_39 = QtWidgets.QLabel(pizzamenu)
        self.label_39.setGeometry(QtCore.QRect(720, 410, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"border-radius: 10px;\n"
"")
        self.label_39.setText("")
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(pizzamenu)
        self.label_40.setGeometry(QtCore.QRect(720, 340, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"border-radius: 10px;\n"
"")
        self.label_40.setText("")
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(pizzamenu)
        self.label_41.setGeometry(QtCore.QRect(720, 270, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"border-radius: 10px;\n"
"")
        self.label_41.setText("")
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(pizzamenu)
        self.label_42.setGeometry(QtCore.QRect(720, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("color: rgb(246, 246, 246);\n"
"background-color: rgb(43, 26, 19);\n"
"border-radius: 10px;\n"
"")
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.pushButton = QtWidgets.QPushButton(pizzamenu)
        self.pushButton.setGeometry(QtCore.QRect(190, 130, 151, 41))
        self.pushButton.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);\n"
"\n"
"border-radius: 10px;\n"
"font: 20pt \"MV Boli\";")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/p.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(pizzamenu)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 130, 141, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);\n"
"border-radius: 10px;\n"
"\n"
"border-radius: 10px;\n"
"font: 20pt \"MV Boli\";")
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(pizzamenu)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 130, 201, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(246, 246, 246);\n"
"border-radius: 10px;\n"
"\n"
"border-radius: 10px;\n"
"font: 20pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(pizzamenu)
        QtCore.QMetaObject.connectSlotsByName(pizzamenu)
        self.Form = pizzamenu
        self.checkBox.clicked.connect(lambda: self.k1(1))
        self.checkBox_2.clicked.connect(lambda: self.k2(2))
        self.checkBox_3.clicked.connect(lambda: self.k3(3))
        self.checkBox_4.clicked.connect(lambda: self.k4(4))

        self.pushButton_5.clicked.connect(self.gitmusterigiris)
        self.pushButton_11.clicked.connect(self.gitmenu)
        self.pushButton_12.clicked.connect(self.gitsepet)
        self.pushButton_18.clicked.connect(self.comp)


        self.checkBox.clicked.connect(lambda: self.buyrun(pizzamenu))
        self.checkBox_2.clicked.connect(lambda: self.buyrunn(pizzamenu))
        self.checkBox_3.clicked.connect(lambda: self.buyrunnn(pizzamenu))
        self.checkBox_4.clicked.connect(lambda: self.buyrunnn(pizzamenu))

    def buyrun(self,pizzamenu):
        if (self.checkBox.isChecked()):
            name = self.checkBox.text()

            quantity = self.textEdit.toPlainText()

            price = self.label_42.text()

            conn = sqlite3.connect('pizza.db')
            query = "INSERT INTO cart (name, quantity, price) VALUES ('%s','%s','%s')" % (name, quantity, price)
            print(query)
            conn.execute(query)
            conn.commit()
            conn.close()

    def buyrunn(self,pizzamenu):
        if (self.checkBox_2.isChecked()):
            name = self.checkBox_2.text()

            quantity = self.textEdit_2.toPlainText()

            price = self.label_41.text()

            conn = sqlite3.connect('pizza.db')
            query = "INSERT INTO cart (name, quantity, price) VALUES ('%s','%s','%s')" % (name, quantity, price)
            print(query)
            conn.execute(query)
            conn.commit()
            conn.close()


    def buyrunnn(self,pizzamenu):
        if (self.checkBox_3.isChecked()):
            name = self.checkBox_3.text()

            quantity = self.textEdit_3.toPlainText()

            price = self.label_40.text()

            conn = sqlite3.connect('pizza.db')
            query = "INSERT INTO cart (name, quantity, price) VALUES ('%s','%s','%s')" % (name, quantity, price)
            print(query)
            conn.execute(query)
            conn.commit()
            conn.close()

    def buyrunnnn(self,pizzamenu):
        if (self.checkBox_4.isChecked()):
            name = self.checkBox_4.text()

            quantity = self.textEdit_4.toPlainText()

            price = self.label_39.text()

            conn = sqlite3.connect('pizza.db')
            query = "INSERT INTO cart (name, quantity, price) VALUES ('%s','%s','%s')" % (name, quantity, price)
            print(query)
            conn.execute(query)
            conn.commit()
            conn.close()

    def retranslateUi(self, pizzamenu):

        _translate = QtCore.QCoreApplication.translate
        pizzamenu.setWindowTitle(_translate("pizzamenu", "Form"))
        self.pushButton_5.setText(_translate("pizzamenu", "LOGOUT"))
        self.pushButton_11.setText(_translate("pizzamenu", "ADD MORE"))
        self.pushButton_12.setText(_translate("pizzamenu", "CART"))
        self.checkBox_3.setText(_translate("pizzamenu", "VEG PIZZA"))
        self.checkBox.setText(_translate("pizzamenu", "MIX PIZZA"))
        self.checkBox_2.setText(_translate("pizzamenu", "MARGARITA PIZZA"))
        self.checkBox_4.setText(_translate("pizzamenu", "CHICKEN PIZZA"))
        self.pushButton_18.setText(_translate("pizzamenu", "Total Cost"))
        self.pushButton.setText(_translate("pizzamenu", "KIND"))
        self.pushButton_2.setText(_translate("pizzamenu", "COST"))
        self.pushButton_3.setText(_translate("pizzamenu", "QUANTITY"))
        self.label_18.setText(_translate("pizzamenu", "30.00"))
        self.label_19.setText(_translate("pizzamenu", "34.00"))
        self.label_20.setText(_translate("pizzamenu", "25.00"))
        self.label_21.setText(_translate("pizzamenu", "40.00"))





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
        content = 'select cost from pizzaa where pizzaID= %d' % id
        res = curs.execute(content)
        for data in res:
            return int(data[0])


from resim import YeniMetinBelgesi_rc


if __name__ == "__main__":


    import sys
    app = QtWidgets.QApplication(sys.argv)
    pizzamenu = QtWidgets.QWidget()
    ui = Ui_pizzamenu()
    ui.setupUi(pizzamenu)
    pizzamenu.show()
    sys.exit(app.exec_())
