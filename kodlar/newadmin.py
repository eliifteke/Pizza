import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem


class Ui_newadmin(object):
    def setupUi(self, newadmin):
        newadmin.setObjectName("newadmin")
        newadmin.resize(651, 550)
        self.pushButton_4 = QtWidgets.QPushButton(newadmin)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 10, 101, 41))
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
        self.pushButton_5 = QtWidgets.QPushButton(newadmin)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 380, 121, 31))
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
      #  self.pushButton_6 = QtWidgets.QPushButton(newadmin)
       # self.pushButton_6.setGeometry(QtCore.QRect(380, 430, 121, 31))
        #self.pushButton_6.setStyleSheet(".QPushButton\n"
#"{\n"
#"background: rgb(170,170, 255);\n"
#"\n"
#"font: 15pt \"8514oem\";\n"
#"border-radius: 10px;\n"
#"}\n"
#"\n"
#".QPushButton:hover\n"
#"{\n"
#"     background-color: rgb(100, 150, 255);\n"
#"}\n"
#"")
 #       self.pushButton_6.setAutoDefault(False)
  #      self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(newadmin)
        self.pushButton_7.setGeometry(QtCore.QRect(380, 480, 121, 31))
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
    #    self.pushButton_8 = QtWidgets.QPushButton(newadmin)
     #   self.pushButton_8.setGeometry(QtCore.QRect(360, 50, 121, 31))
      #  self.pushButton_8.setStyleSheet(".QPushButton\n"
#"{\n"
#"background: rgb(170,170, 255);\n"
#"\n"
#"font: 15pt \"8514oem\";\n"
#"border-radius: 10px;\n"
#"}\n"
#"\n"
#".QPushButton:hover\n"
#"{\n"
#"     background-color: rgb(100, 150, 255);\n"
#"}\n"
#"")
 #       self.pushButton_8.setAutoDefault(False)
  #      self.pushButton_8.setObjectName("pushButton_8")
        self.tableWidget = QtWidgets.QTableWidget(newadmin)
        self.tableWidget.setGeometry(QtCore.QRect(30, 110, 501, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.label_4 = QtWidgets.QLabel(newadmin)
        self.label_4.setGeometry(QtCore.QRect(70, 370, 60, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(newadmin)
        self.label_5.setGeometry(QtCore.QRect(50, 490, 101, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(newadmin)
        self.label_6.setGeometry(QtCore.QRect(50, 410, 111, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(newadmin)
        self.label_7.setGeometry(QtCore.QRect(50, 450, 101, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEdit = QtWidgets.QTextEdit(newadmin)
        self.textEdit.setGeometry(QtCore.QRect(160, 370, 171, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(newadmin)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 410, 171, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(newadmin)
        self.textEdit_3.setGeometry(QtCore.QRect(160, 450, 171, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(newadmin)
        self.textEdit_4.setGeometry(QtCore.QRect(160, 490, 171, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        #self.textEdit_5 = QtWidgets.QTextEdit(newadmin)
        #self.textEdit_5.setGeometry(QtCore.QRect(170, 50, 171, 31))
       # self.textEdit_5.setObjectName("textEdit_5")
        self.label_8 = QtWidgets.QLabel(newadmin)
        self.label_8.setGeometry(QtCore.QRect(70, 50, 91, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_9 = QtWidgets.QPushButton(newadmin)
        self.pushButton_9.setGeometry(QtCore.QRect(60, 320, 121, 31))
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

        self.retranslateUi(newadmin)
        QtCore.QMetaObject.connectSlotsByName(newadmin)

        self.Form = newadmin
        self.pushButton_5.clicked.connect(lambda : self.adminekle(newadmin))
        self.pushButton_4.clicked.connect(lambda :self.gitmenu(newadmin))
        self.pushButton_9.clicked.connect(lambda : self.uyelist(newadmin))
        self.pushButton_7.clicked.connect(lambda : self.delete(newadmin))
#        self.pushButton_8.clicked.connect(self.ara)

        #self.pushButton_6.clicked.connect(self.update)
        #self.tableWidget.itemSelectionChanged.connect(self.goster)



    def retranslateUi(self, newadmin):
        _translate = QtCore.QCoreApplication.translate
        newadmin.setWindowTitle(_translate("newadmin", "Form"))
        self.pushButton_4.setText(_translate("newadmin", "BACK"))
        self.pushButton_5.setText(_translate("newadmin", "ADD"))
        #self.pushButton_6.setText(_translate("newadmin", "UPDATE"))
        self.pushButton_7.setText(_translate("newadmin", "DELETE"))
        #self.pushButton_8.setText(_translate("newadmin", "SEARCH"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("newadmin", "name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("newadmin", "surname"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("newadmin", "username"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("newadmin", "password"))
        self.label_4.setText(_translate("newadmin", "Name :"))
        self.label_5.setText(_translate("newadmin", "Password :"))
        self.label_6.setText(_translate("newadmin", "Surname :"))
        self.label_7.setText(_translate("newadmin", "Username :"))
       # self.label_8.setText(_translate("newadmin", "Username"))
        self.pushButton_9.setText(_translate("newadmin", "DISPLAY"))

        self.tableWidget.doubleClicked.connect(self.tiklanmisSatir)


    def tiklanmisSatir(self):
        print("Table clicked")


    def adminekle(self,newadmin):
        import veribaglan
        name = self.textEdit.toPlainText()
        surname = self.textEdit_2.toPlainText()
        username = self.textEdit_3.toPlainText()
        password = self.textEdit_4.toPlainText()

        veri = veribaglan.musteriekle(name, surname, username, password)
        results=QMessageBox.warning(newadmin,'New Admin','added succesfully')
        newadmin.show()
        if not veri:
            return


    def ara(self):
        searchroll=""
        searchroll= self. textEdit_5.toPlainText()
        try:
            conn=sqlite3.connect("pizza.db")
            c=conn.cursor()
            result=c.execute("SELECT * FROM musteri WHERE username= " +str(searchroll))
            row=result.fetchone()

            searchresult=str(row[0])
            self.textEdit.setText(searchresult)
            self.textEdit_2.setText(str(row[1]))
            self.textEdit_3.setText(str(row[2]))
            self.textEdit_4.setText(str(row[3]))

            conn.close()

        except Exception:
            print("no find")

    def arama(self):
        searchroll=""
        searchroll= self. textEdit_5.toPlainText()
        try:
            conn=sqlite3.connect("pizza.db")
            c=conn.cursor()
            result=c.execute("SELECT * FROM musteri WHERE username= " +str(searchroll))
            row=result.fetchone()

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                self.connection.close()
                conn.close()
        except Exception:
            print()



    def update(self):
        con = sqlite3.connect('pizza.db')
        co = con.cursor()
        name = self.textEdit.toPlainText()
        surname = self.textEdit_2.toPlainText()
        username = self.textEdit_3.toPlainText()
        password = self.textEdit_4.toPlainText()
        con.execute('''UPDATE musteri SET surname=?, username=?, password=? WHERE name=? ''',
                    (self.textEdit_2.toPlainText(), self.textEdit_3.toPlainText(), self.textEdit_4.toPlainText(),self.textEdit.toPlainText()))
        con.commit()




    def gitmenu(self,newadmin):
        from musterigiris import Ui_musterigiris
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_musterigiris()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için

    def uyelist(self,newadmin):
        self.connection = sqlite3.connect("pizza.db")
        query = "SELECT * FROM musteri"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()


    def delete(self,newadmin):
        conn = sqlite3.connect('pizza.db')
        curs = conn.cursor()
        content = 'SELECT *FROM musteri'
        res = curs.execute(content)
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                name = data[0]
                surname = data[1]
                curs.execute('''DELETE FROM musteri WHERE name=? AND surname=?''', (name, surname))
                conn.commit()
        result = QMessageBox.warning(newadmin, 'Message', 'Deleted User!')



from resim import YeniMetinBelgesi_rc




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newadmin = QtWidgets.QWidget()
    ui = Ui_newadmin()
    ui.setupUi(newadmin)
    newadmin.show()
    sys.exit(app.exec_())
