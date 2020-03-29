# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_about(object):
    def setupUi(self, about):
        about.setObjectName("about")
        about.resize(697, 363)
        about.setStyleSheet("#about{\n"
"border-image: url(:/newPrefix/pizza.jpg);\n"
"}")
        self.pushButton_3 = QtWidgets.QPushButton(about)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 30, 291, 71))
        self.pushButton_3.setStyleSheet(".QPushButton{\n"
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
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/order.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(about)
        self.textEdit.setGeometry(QtCore.QRect(50, 120, 611, 201))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_4 = QtWidgets.QPushButton(about)
        self.pushButton_4.setGeometry(QtCore.QRect(580, 10, 101, 41))
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

        self.retranslateUi(about)
        QtCore.QMetaObject.connectSlotsByName(about)

        self.Form = about
        self.pushButton_4.clicked.connect(self.gitmenu)

    def retranslateUi(self, about):
        _translate = QtCore.QCoreApplication.translate
        about.setWindowTitle(_translate("about", "Form"))
        self.pushButton_3.setText(_translate("about", "ABOUT"))
        self.textEdit.setHtml(_translate("about", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:30px; background-color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:30px; background-color:#ffffff;\"><span style=\" font-family:\'Hind Vadodara,sans-serif\'; font-size:14pt; color:#505061; background-color:#ffffff;\">1996 yılında Türkiyede ilk şubesini Istanbul, Ulus\'ta açan Come To Pizza\'s Türkiye olarak şu an, İstanbul, İzmir, Ankara ve Bursa başta olmak üzere 69 ile yayılmış 530 şubemiz ile Türkiye pizza endüstrisine öncülük ediyoruz. </span></p></body></html>"))
        self.pushButton_4.setText(_translate("about", "BACK"))

    def gitmenu(self):
        from musterigiris import Ui_musterigiris
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_musterigiris()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.Form.close()  # önceki sayfayı kapatmak için
from resim import YeniMetinBelgesi_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    about = QtWidgets.QWidget()
    ui = Ui_about()
    ui.setupUi(about)
    about.show()
    sys.exit(app.exec_())
