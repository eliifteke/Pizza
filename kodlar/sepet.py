# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sepet.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_sepet(object):
    def comp(self):
        total = 0

        if (self.checkBox.isChecked()):
            a = self.label_42.text()
            total += float(a)
            print(total)
            self.label_2.setText('%0.2f' % total)


    def setupUi(self, sepet):
        sepet.setObjectName("sepet")
        sepet.resize(763, 622)
        sepet.setStyleSheet("#sepet{\n"
"border-image: url(:/newPrefix/pizza.jpg);\n"
"}")
        self.pushButton_5 = QtWidgets.QPushButton(sepet)
        self.pushButton_5.setGeometry(QtCore.QRect(580, 40, 131, 41))
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
        self.pushButton_6 = QtWidgets.QPushButton(sepet)
        self.pushButton_6.setGeometry(QtCore.QRect(420, 460, 131, 41))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(".QPushButton\n"
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
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton = QtWidgets.QPushButton(sepet)
        self.pushButton.setGeometry(QtCore.QRect(40, 90, 341, 71))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(".QPushButton{\n"
"font: 25pt \"Ink Free\";\n"
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
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/siparis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(35, 35))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(sepet)
        self.tableWidget.setGeometry(QtCore.QRect(10, 200, 381, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton_18 = QtWidgets.QPushButton(sepet)
        self.pushButton_18.setGeometry(QtCore.QRect(420, 290, 171, 51))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resim/money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_18.setIcon(icon1)
        self.pushButton_18.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_2 = QtWidgets.QLabel(sepet)
        self.label_2.setGeometry(QtCore.QRect(600, 290, 111, 51))
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
        self.pushButton_11 = QtWidgets.QPushButton(sepet)
        self.pushButton_11.setGeometry(QtCore.QRect(570, 460, 131, 41))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/more.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon2)
        self.pushButton_11.setAutoDefault(False)
        self.pushButton_11.setObjectName("pushButton_11")

        self.retranslateUi(sepet)
        QtCore.QMetaObject.connectSlotsByName(sepet)
        self.Form = sepet
        self.pushButton_5.clicked.connect(self.gitmusterigiris)
        self.pushButton_6.clicked.connect(self.display)
        self.pushButton_11.clicked.connect(self.gitmenu)
        self.pushButton_18.clicked.connect(self.comp)




    def retranslateUi(self, sepet):
        _translate = QtCore.QCoreApplication.translate
        sepet.setWindowTitle(_translate("sepet", "Form"))
        self.pushButton_5.setText(_translate("sepet", "LOGOUT"))
        self.pushButton_6.setText(_translate("sepet", "DISPLAY"))
        self.pushButton.setText(_translate("sepet", "ORDERS"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("sepet", "name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("sepet", "quantity"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("sepet", "price"))
        self.pushButton_18.setText(_translate("sepet", "Total Cost"))
        self.pushButton_11.setText(_translate("sepet", "ADD MORE"))

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


    def display(self):
        self.connection = sqlite3.connect("pizza.db")
        query = "SELECT * FROM cart"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()


from resim import YeniMetinBelgesi_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sepet = QtWidgets.QWidget()
    ui = Ui_sepet()
    ui.setupUi(sepet)
    sepet.show()
    sys.exit(app.exec_())
