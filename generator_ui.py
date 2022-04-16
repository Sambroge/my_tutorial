# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(545, 625)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("background-color: rgb(170, 85, 127);\n"
"border-radius: 20;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: rgb(255, 249, 60);")
        self.label_3.setLineWidth(2)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame)
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    font: 10pt \"Lucida Console\";\n"
"QCheckBox::indicator {\n"
"    width: 100px;\n"
"    height: 13px;\n"
"}")
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Console\";")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Console\";")
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Console\";")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Console\";")
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Lucida Console\";")
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spin_Box2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_Box2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spin_Box2.setKeyboardTracking(True)
        self.spin_Box2.setProperty("showGroupSeparator", False)
        self.spin_Box2.setMinimum(5)
        self.spin_Box2.setMaximum(20)
        self.spin_Box2.setObjectName("spin_Box2")
        self.horizontalLayout.addWidget(self.spin_Box2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spin_Box = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_Box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spin_Box.setSuffix("")
        self.spin_Box.setPrefix("")
        self.spin_Box.setMinimum(1)
        self.spin_Box.setMaximum(20)
        self.spin_Box.setObjectName("spin_Box")
        self.horizontalLayout_2.addWidget(self.spin_Box)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(55)
        sizePolicy.setVerticalStretch(37)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid;\n"
"border-color: rgb(170, 85, 127);\n"
"border-radius: 20;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(170, 85, 127);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid;\n"
"border-color: rgb(170, 85, 127);\n"
"border-radius: 20;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(170, 85, 127);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 270))
        self.textBrowser.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(170, 85, 127);\n"
"border-radius: 10")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 545, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генератор паролей"))
        self.label_3.setText(_translate("MainWindow", "Генератор Ваших паролей !"))
        self.checkBox_3.setText(_translate("MainWindow", "Использовать цифры в пароле"))
        self.checkBox.setText(_translate("MainWindow", "Использовать буквы английского языка нижнего регистра в пароле"))
        self.checkBox_4.setText(_translate("MainWindow", "Использовать буквы английского языка верхнего регистра в пароле"))
        self.checkBox_2.setText(_translate("MainWindow", "Использовать символы пунктуации в пароле"))
        self.checkBox_5.setText(_translate("MainWindow", "Удалить неоднозначные символы (\'i\' \'l\' \'1\' \'L\' \'o\' \'0\' \'O\')"))
        self.checkBox_6.setText(_translate("MainWindow", "Сохранить пароли в текстовый документ корневой папки"))
        self.label.setText(_translate("MainWindow", "Введи количество символов в пароле:"))
        self.label_2.setText(_translate("MainWindow", "Введи количество паролей:"))
        self.pushButton_2.setText(_translate("MainWindow", "Сброс"))
        self.pushButton.setText(_translate("MainWindow", "Сгенерировать"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())