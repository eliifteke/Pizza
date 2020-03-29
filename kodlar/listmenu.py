import  sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox


class Ui_listmenu(object):
    def setupUi(self, listmenu):
        listmenu.setObjectName("listmenu")
        listmenu.resize(686, 809)
        listmenu.setStyleSheet("#listmenu{\n"
"border-image: url(resim/list.jpg);\n"
"}")
        self.pushButton_4 = QtWidgets.QPushButton(listmenu)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 70, 101, 41))
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
        self.pushButton_5 = QtWidgets.QPushButton(listmenu)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 70, 131, 41))
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
        self.tableWidget = QtWidgets.QTableWidget(listmenu)
        self.tableWidget.setGeometry(QtCore.QRect(180, 150, 311, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton_9 = QtWidgets.QPushButton(listmenu)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 590, 121, 31))
        self.pushButton_9.setStyleSheet(".QPushButton\n"
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
        self.pushButton_9.setAutoDefault(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_6 = QtWidgets.QPushButton(listmenu)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 590, 121, 31))
        self.pushButton_6.setStyleSheet(".QPushButton\n"
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
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(listmenu)
        self.pushButton_7.setGeometry(QtCore.QRect(420, 590, 121, 31))
        self.pushButton_7.setStyleSheet(".QPushButton\n"
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
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit = QtWidgets.QLineEdit(listmenu)
        self.lineEdit.setGeometry(QtCore.QRect(200, 660, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText('NAME')

        self.lineEdit_2 = QtWidgets.QLineEdit(listmenu)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 660, 131, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText('COST')


        self.retranslateUi(listmenu)
        QtCore.QMetaObject.connectSlotsByName(listmenu)

        self.Form = listmenu
        self.pushButton_4.clicked.connect(self.gitmenu)
        self.pushButton_5.clicked.connect(self.gitmusterigiris)
        self.pushButton_6.clicked.connect(lambda : self.ekle(listmenu))
        self.pushButton_7.clicked.connect(lambda :self.sil(listmenu))
        self.pushButton_9.clicked.connect(lambda :self.goster(listmenu))

    def retranslateUi(self, listmenu):
        _translate = QtCore.QCoreApplication.translate
        listmenu.setWindowTitle(_translate("listmenu", "Form"))
        self.pushButton_4.setText(_translate("listmenu", "BACK"))
        self.pushButton_5.setText(_translate("listmenu", "LOGOUT"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("listmenu", "name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("listmenu", "cost"))
        self.pushButton_9.setText(_translate("listmenu", "DISPLAY"))
        self.pushButton_6.setText(_translate("listmenu", "ADD"))
        self.pushButton_7.setText(_translate("listmenu", "DELETE"))

    def gitmenu(self):
        from menu import Ui_menu
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_menu()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için

    def gitmusterigiris(self):
        from musterigiris import Ui_musterigiris
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_musterigiris()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için

    def ekle(self,listmenu):
        import veribaglan
        username = self.lineEdit.text()
        cost = self.lineEdit_2.text()


        results = QMessageBox.warning(listmenu, 'LIST', 'added menu')
        listmenu.show()
        veri = veribaglan.ekle(username, cost)

        if not veri:
            return;


    def sil(self,listmenu):
        conn = sqlite3.connect('pizza.db')
        curs = conn.cursor()
        content = 'SELECT *FROM list'
        res = curs.execute(content)
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                name = data[0]
                cost = data[1]
                curs.execute('''DELETE FROM list WHERE name=? AND cost=?''', (name, cost))
                conn.commit()
        result = QMessageBox.warning(listmenu, 'Message', 'Deleted Menu!')


    def goster(self, listmenu):
        self.connection = sqlite3.connect("pizza.db")
        query = "SELECT * FROM list"
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
    listmenu = QtWidgets.QWidget()
    ui = Ui_listmenu()
    ui.setupUi(listmenu)
    listmenu.show()
    sys.exit(app.exec_())
