# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'itog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_itog(object):
    def setupUi(self, itog):
        itog.setObjectName("itog")
        itog.resize(989, 638)
        self.label = QtWidgets.QLabel(itog)
        self.label.setGeometry(QtCore.QRect(200, 20, 561, 161))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(itog)
        self.label_2.setGeometry(QtCore.QRect(370, 190, 251, 121))
        self.label_2.setStyleSheet("font: 26pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 49);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(itog)
        self.label_3.setGeometry(QtCore.QRect(130, 320, 701, 151))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(itog)
        self.pushButton.setGeometry(QtCore.QRect(240, 500, 481, 71))
        self.pushButton.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(2, 45, 0);\n"
"background-color: rgb(255, 170, 255);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(itog)
        QtCore.QMetaObject.connectSlotsByName(itog)

    def retranslateUi(self, itog):
        _translate = QtCore.QCoreApplication.translate
        itog.setWindowTitle(_translate("itog", "Form"))
        self.label.setText(_translate("itog", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#000038;\">Поздравляем, вы завершили тест! </span></p><p align=\"center\"><span style=\" font-size:24pt; color:#000038;\">Ваш результат:</span></p></body></html>"))
        self.label_2.setText(_translate("itog", "TextLabel"))
        self.label_3.setText(_translate("itog", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#000043;\">Если вас не устраивает ваш</span></p><p align=\"center\"><span style=\" font-size:24pt; color:#000043;\">результат или вы хотите пройти</span></p><p align=\"center\"><span style=\" font-size:24pt; color:#000043;\">тест на другую тему, то просто </span></p></body></html>"))
        self.pushButton.setText(_translate("itog", "Нажмите на эту кнопочку :)"))
