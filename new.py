# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cala.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import math
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 2, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 2, 1, 1)
        self.page = QtWidgets.QStackedWidget(self.centralwidget)
        self.page.setObjectName("page")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.gridLayout = QtWidgets.QGridLayout(self.main_page)
        self.gridLayout.setObjectName("gridLayout")
        self.chooseButton = QtWidgets.QPushButton(self.main_page)
        self.chooseButton.setObjectName("chooseButton")
        self.gridLayout.addWidget(self.chooseButton, 5, 0, 1, 1)
        self.w_radioButton = QtWidgets.QRadioButton(self.main_page)
        self.w_radioButton.setObjectName("w_radioButton")
        self.gridLayout.addWidget(self.w_radioButton, 1, 0, 1, 1)
        self.t_radioButton = QtWidgets.QRadioButton(self.main_page)
        self.t_radioButton.setObjectName("t_radioButton")
        self.gridLayout.addWidget(self.t_radioButton, 3, 0, 1, 1)
        self.k_radioButton = QtWidgets.QRadioButton(self.main_page)
        self.k_radioButton.setObjectName("k_radioButton")
        self.gridLayout.addWidget(self.k_radioButton, 4, 0, 1, 1)
        self.s_radioButton = QtWidgets.QRadioButton(self.main_page)
        self.s_radioButton.setObjectName("s_radioButton")
        self.gridLayout.addWidget(self.s_radioButton, 2, 0, 1, 1)
        self.page.addWidget(self.main_page)
        self.w_page = QtWidgets.QWidget()
        self.w_page.setObjectName("w_page")
        self.BackButton = QtWidgets.QPushButton(self.w_page)
        self.BackButton.setGeometry(QtCore.QRect(10, 10, 238, 26))
        self.BackButton.setObjectName("BackButton")
        self.label = QtWidgets.QLabel(self.w_page)
        self.label.setGeometry(QtCore.QRect(20, 50, 191, 16))
        self.label.setObjectName("label")
        self.w_Box = QtWidgets.QDoubleSpinBox(self.w_page)
        self.w_Box.setGeometry(QtCore.QRect(90, 80, 62, 22))
        self.w_Box.setObjectName("w_Box")
        self.w_calculate = QtWidgets.QPushButton(self.w_page)
        self.w_calculate.setGeometry(QtCore.QRect(71, 110, 91, 26))
        self.w_calculate.setObjectName("w_calculate")
        self.label_2 = QtWidgets.QLabel(self.w_page)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 141, 16))
        self.label_2.setObjectName("label_2")
        self.w_area = QtWidgets.QLCDNumber(self.w_page)
        self.w_area.setGeometry(QtCore.QRect(110, 147, 64, 23))
        self.w_area.setObjectName("w_area")
        self.page.addWidget(self.w_page)
        self.s_page = QtWidgets.QWidget()
        self.s_page.setObjectName("s_page")
        self.BackButton_2 = QtWidgets.QPushButton(self.s_page)
        self.BackButton_2.setGeometry(QtCore.QRect(10, 10, 238, 26))
        self.BackButton_2.setObjectName("BackButton_2")
        self.label_3 = QtWidgets.QLabel(self.s_page)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.s_page)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.s_page)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 71, 16))
        self.label_5.setObjectName("label_5")
        self.s_Box_1 = QtWidgets.QDoubleSpinBox(self.s_page)
        self.s_Box_1.setGeometry(QtCore.QRect(80, 47, 62, 22))
        self.s_Box_1.setObjectName("s_Box_1")
        self.s_Box_2 = QtWidgets.QDoubleSpinBox(self.s_page)
        self.s_Box_2.setGeometry(QtCore.QRect(80, 77, 62, 22))
        self.s_Box_2.setObjectName("s_Box_2")
        self.s_Box_3 = QtWidgets.QDoubleSpinBox(self.s_page)
        self.s_Box_3.setGeometry(QtCore.QRect(80, 107, 62, 22))
        self.s_Box_3.setObjectName("s_Box_3")
        self.s_calculate = QtWidgets.QPushButton(self.s_page)
        self.s_calculate.setGeometry(QtCore.QRect(150, 80, 101, 26))
        self.s_calculate.setObjectName("s_calculate")
        self.label_6 = QtWidgets.QLabel(self.s_page)
        self.label_6.setGeometry(QtCore.QRect(10, 150, 91, 16))
        self.label_6.setObjectName("label_6")
        self.s_area = QtWidgets.QLCDNumber(self.s_page)
        self.s_area.setGeometry(QtCore.QRect(110, 147, 64, 23))
        self.s_area.setObjectName("s_area")
        self.label_14 = QtWidgets.QLabel(self.s_page)
        self.label_14.setGeometry(QtCore.QRect(160, 50, 81, 20))
        self.label_14.setStyleSheet("font: 13pt \"BPG Banner\";")
        self.label_14.setObjectName("label_14")
        self.page.addWidget(self.s_page)
        self.t_page = QtWidgets.QWidget()
        self.t_page.setObjectName("t_page")
        self.BackButton_3 = QtWidgets.QPushButton(self.t_page)
        self.BackButton_3.setGeometry(QtCore.QRect(10, 10, 238, 26))
        self.BackButton_3.setObjectName("BackButton_3")
        self.label_7 = QtWidgets.QLabel(self.t_page)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 58, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.t_page)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 58, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.t_page)
        self.label_9.setGeometry(QtCore.QRect(10, 110, 61, 16))
        self.label_9.setObjectName("label_9")
        self.t_Box_1 = QtWidgets.QDoubleSpinBox(self.t_page)
        self.t_Box_1.setGeometry(QtCore.QRect(80, 47, 62, 22))
        self.t_Box_1.setObjectName("t_Box_1")
        self.t_Box_2 = QtWidgets.QDoubleSpinBox(self.t_page)
        self.t_Box_2.setGeometry(QtCore.QRect(80, 77, 62, 22))
        self.t_Box_2.setObjectName("t_Box_2")
        self.t_Box_3 = QtWidgets.QDoubleSpinBox(self.t_page)
        self.t_Box_3.setGeometry(QtCore.QRect(80, 107, 62, 22))
        self.t_Box_3.setObjectName("t_Box_3")
        self.label_10 = QtWidgets.QLabel(self.t_page)
        self.label_10.setGeometry(QtCore.QRect(10, 150, 71, 16))
        self.label_10.setObjectName("label_10")
        self.t_area = QtWidgets.QLCDNumber(self.t_page)
        self.t_area.setGeometry(QtCore.QRect(110, 147, 64, 23))
        self.t_area.setObjectName("t_area")
        self.t_calculate = QtWidgets.QPushButton(self.t_page)
        self.t_calculate.setGeometry(QtCore.QRect(150, 80, 101, 26))
        self.t_calculate.setObjectName("t_calculate")
        self.label_11 = QtWidgets.QLabel(self.t_page)
        self.label_11.setGeometry(QtCore.QRect(170, 50, 71, 20))
        self.label_11.setStyleSheet("font: 13pt \"BPG Banner\";")
        self.label_11.setObjectName("label_11")
        self.page.addWidget(self.t_page)
        self.k_page = QtWidgets.QWidget()
        self.k_page.setObjectName("k_page")
        self.BackButton_4 = QtWidgets.QPushButton(self.k_page)
        self.BackButton_4.setGeometry(QtCore.QRect(10, 10, 238, 26))
        self.BackButton_4.setObjectName("BackButton_4")
        self.k_calculate = QtWidgets.QPushButton(self.k_page)
        self.k_calculate.setGeometry(QtCore.QRect(150, 80, 101, 26))
        self.k_calculate.setObjectName("k_calculate")
        self.label_12 = QtWidgets.QLabel(self.k_page)
        self.label_12.setGeometry(QtCore.QRect(10, 50, 58, 16))
        self.label_12.setObjectName("label_12")
        self.t_Box = QtWidgets.QDoubleSpinBox(self.k_page)
        self.t_Box.setGeometry(QtCore.QRect(80, 47, 62, 22))
        self.t_Box.setObjectName("t_Box")
        self.label_13 = QtWidgets.QLabel(self.k_page)
        self.label_13.setGeometry(QtCore.QRect(10, 150, 71, 16))
        self.label_13.setObjectName("label_13")
        self.k_area = QtWidgets.QLCDNumber(self.k_page)
        self.k_area.setGeometry(QtCore.QRect(110, 147, 64, 23))
        self.k_area.setObjectName("k_area")
        self.label_15 = QtWidgets.QLabel(self.k_page)
        self.label_15.setGeometry(QtCore.QRect(165, 50, 71, 16))
        self.label_15.setStyleSheet("font: 13pt \"BPG Banner\";")
        self.label_15.setObjectName("label_15")
        self.page.addWidget(self.k_page)
        self.gridLayout_2.addWidget(self.page, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.page.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chooseButton.setText(_translate("MainWindow", "არჩევა"))
        self.w_radioButton.setText(_translate("MainWindow", "წრე"))
        self.t_radioButton.setText(_translate("MainWindow", "ტრაპეცია"))
        self.k_radioButton.setText(_translate("MainWindow", "კვადრატი"))
        self.s_radioButton.setText(_translate("MainWindow", "სამკუთხედი"))
        self.BackButton.setText(_translate("MainWindow", "უკან"))
        self.label.setText(_translate("MainWindow", "შეიყვანეთ წრის რადიუსი:"))
        self.w_calculate.setText(_translate("MainWindow", "გამოთვლა"))
        self.label_2.setText(_translate("MainWindow", "ფართობია:"))
        self.BackButton_2.setText(_translate("MainWindow", "უკან"))
        self.label_3.setText(_translate("MainWindow", "გვერდი 1:"))
        self.label_4.setText(_translate("MainWindow", "გვერდი 2:"))
        self.label_5.setText(_translate("MainWindow", "გვერდი 3:"))
        self.s_calculate.setText(_translate("MainWindow", "გამოთვლა"))
        self.label_6.setText(_translate("MainWindow", "ფართობია:"))
        self.label_14.setText(_translate("MainWindow", "სამკუთხედი"))
        self.BackButton_3.setText(_translate("MainWindow", "უკან"))
        self.label_7.setText(_translate("MainWindow", "ფუძე 1:"))
        self.label_8.setText(_translate("MainWindow", "ფუძე 2:"))
        self.label_9.setText(_translate("MainWindow", "სიმაღლე:"))
        self.label_10.setText(_translate("MainWindow", "ფართობია:"))
        self.t_calculate.setText(_translate("MainWindow", "გამოთვლა"))
        self.label_11.setText(_translate("MainWindow", "ტრაპეცია"))
        self.BackButton_4.setText(_translate("MainWindow", "უკან"))
        self.k_calculate.setText(_translate("MainWindow", "გამოთვლა"))
        self.label_12.setText(_translate("MainWindow", "გვერდი"))
        self.label_13.setText(_translate("MainWindow", "ფართობია:"))
        self.label_15.setText(_translate("MainWindow", "კვადრატი"))

    def choose(self):
        if self.w_radioButton.isChecked():
            self.page.setCurrentIndex(1)
        if self.s_radioButton.isChecked():
            self.page.setCurrentIndex(2)
        if self.t_radioButton.isChecked():
            self.page.setCurrentIndex(3)
        if self.k_radioButton.isChecked():
            self.page.setCurrentIndex(4)
        if self.BackButton.isChecked() or self.BackButton_2.isChecked() or self.BackButton_3.isChecked() or self.BackButton_4.isChecked():
            self.page.setCurrentIndex(0)


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.chooseButton.clicked.connect(self.ui.choose)
        self.ui.BackButton.clicked.connect(self.goToMainPage)
        self.ui.BackButton_2.clicked.connect(self.goToMainPage)
        self.ui.BackButton_3.clicked.connect(self.goToMainPage)
        self.ui.BackButton_4.clicked.connect(self.goToMainPage)
        self.ui.w_calculate.clicked.connect(self.calculateWArea)
        self.ui.s_calculate.clicked.connect(self.calculateSArea)
        self.ui.t_calculate.clicked.connect(self.calculateTArea)
        self.ui.k_calculate.clicked.connect(self.calculateKArea)
    def goToMainPage(self):
        self.ui.page.setCurrentIndex(0)

    def calculateWArea(self):
        radius = self.ui.w_Box.value()
        area = 3.14159 * radius ** 2
        self.ui.w_area.display(area)
    def calculateSArea(self):
        p1 = self.ui.s_Box_1.value()
        p2 = self.ui.s_Box_2.value()
        p3 = self.ui.s_Box_3.value()
        p=(p1+p2+p3)/2
        area = math.sqrt(p * (p - p1) * (p - p2) * (p - p3))
        self.ui.s_area.display(area)

    def calculateTArea(self):
        p1 = self.ui.t_Box_1.value()
        p2 = self.ui.t_Box_2.value()
        p3 = self.ui.t_Box_3.value()
        area =((p1+p2)/2)*p3
        self.ui.t_area.display(area)
    def calculateKArea(self):
        p1=self.ui.t_Box.value()
        area=4*p1
        self.ui.k_area.display(area)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    my_main_window = MyMainWindow()
    my_main_window.show()
    sys.exit(app.exec_())



