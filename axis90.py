# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doubleaxis.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(404, 400)
        MainWindow.setStyleSheet("QWidget{background-color:black;}\n"
"QFrame{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: white;\n"
"    color: white; \n"
"    background-color:black;\n"
"}\n"
"QLCDNumber{\n"
"   color: white; \n"
"   background-color:black; \n"
"   border-width: 0px;\n"
"}\n"
"QLabel\n"
" {\n"
"   color: white; \n"
"   background-color:black; \n"
"   border-width: 0px;\n"
"   font-weight: bold;\n"
"  }\n"
"QRadioButton\n"
" {\n"
"   color: white; \n"
"   background-color:black; \n"
"   border-width: 0px;\n"
"   font-weight: bold;\n"
"  }\n"
"QRadioButton:hover {color: yellow;}\n"
"QSpinBox{color: white; background-color:black;}\n"
"QPushButton {\n"
"   background-color: black;\n"
"   color: white;\n"
"   border-style: outset;\n"
"   border-width: 2px;\n"
"   border-radius: 10px;\n"
"   border-color: white;\n"
"   padding: 6px;\n"
"   font-weight: bold;\n"
"}\n"
"QPushButton:hover {color: yellow;}\n"
"QLCDNumber {color: lightblue;}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.StepsBox = QtWidgets.QSpinBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StepsBox.sizePolicy().hasHeightForWidth())
        self.StepsBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.StepsBox.setFont(font)
        self.StepsBox.setMinimum(1)
        self.StepsBox.setMaximum(10000)
        self.StepsBox.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.StepsBox.setProperty("value", 16)
        self.StepsBox.setObjectName("StepsBox")
        self.verticalLayout_2.addWidget(self.StepsBox)
        self.gridLayout.addWidget(self.frame_3, 0, 3, 1, 1)
        self.LeftButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftButton.sizePolicy().hasHeightForWidth())
        self.LeftButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.LeftButton.setFont(font)
        self.LeftButton.setObjectName("LeftButton")
        self.gridLayout.addWidget(self.LeftButton, 1, 0, 1, 1)
        self.DownButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.DownButton.setFont(font)
        self.DownButton.setObjectName("DownButton")
        self.gridLayout.addWidget(self.DownButton, 2, 1, 1, 1)
        self.ResetButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResetButton.sizePolicy().hasHeightForWidth())
        self.ResetButton.setSizePolicy(sizePolicy)
        self.ResetButton.setObjectName("ResetButton")
        self.gridLayout.addWidget(self.ResetButton, 2, 0, 1, 1)
        self.RightButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightButton.sizePolicy().hasHeightForWidth())
        self.RightButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.RightButton.setFont(font)
        self.RightButton.setObjectName("RightButton")
        self.gridLayout.addWidget(self.RightButton, 1, 3, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.YlcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.YlcdNumber.setStyleSheet("")
        self.YlcdNumber.setDigitCount(6)
        self.YlcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.YlcdNumber.setObjectName("YlcdNumber")
        self.verticalLayout.addWidget(self.YlcdNumber)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.XlcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.XlcdNumber.setDigitCount(6)
        self.XlcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.XlcdNumber.setObjectName("XlcdNumber")
        self.verticalLayout.addWidget(self.XlcdNumber)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ManualButton = QtWidgets.QRadioButton(self.frame_2)
        self.ManualButton.setObjectName("ManualButton")
        self.verticalLayout_3.addWidget(self.ManualButton)
        self.AutoKeepButton = QtWidgets.QRadioButton(self.frame_2)
        self.AutoKeepButton.setObjectName("AutoKeepButton")
        self.verticalLayout_3.addWidget(self.AutoKeepButton)
        self.AutoScanButton = QtWidgets.QRadioButton(self.frame_2)
        self.AutoScanButton.setObjectName("AutoScanButton")
        self.verticalLayout_3.addWidget(self.AutoScanButton)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.UpButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UpButton.sizePolicy().hasHeightForWidth())
        self.UpButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.UpButton.setFont(font)
        self.UpButton.setStyleSheet("")
        self.UpButton.setObjectName("UpButton")
        self.gridLayout.addWidget(self.UpButton, 0, 1, 1, 1)
        self.ReturnButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ReturnButton.sizePolicy().hasHeightForWidth())
        self.ReturnButton.setSizePolicy(sizePolicy)
        self.ReturnButton.setObjectName("ReturnButton")
        self.gridLayout.addWidget(self.ReturnButton, 2, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ManualButton, self.AutoKeepButton)
        MainWindow.setTabOrder(self.AutoKeepButton, self.AutoScanButton)
        MainWindow.setTabOrder(self.AutoScanButton, self.UpButton)
        MainWindow.setTabOrder(self.UpButton, self.StepsBox)
        MainWindow.setTabOrder(self.StepsBox, self.LeftButton)
        MainWindow.setTabOrder(self.LeftButton, self.RightButton)
        MainWindow.setTabOrder(self.RightButton, self.ResetButton)
        MainWindow.setTabOrder(self.ResetButton, self.DownButton)
        MainWindow.setTabOrder(self.DownButton, self.ReturnButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Steps per Click"))
        self.LeftButton.setText(_translate("MainWindow", "◁"))
        self.LeftButton.setShortcut(_translate("MainWindow", "Left"))
        self.DownButton.setText(_translate("MainWindow", "▽"))
        self.DownButton.setShortcut(_translate("MainWindow", "Down"))
        self.ResetButton.setText(_translate("MainWindow", "Counters Reset"))
        self.RightButton.setText(_translate("MainWindow", "▷"))
        self.RightButton.setShortcut(_translate("MainWindow", "Right"))
        self.label.setText(_translate("MainWindow", "Vertical:"))
        self.label_2.setText(_translate("MainWindow", "Horizontal:"))
        self.ManualButton.setText(_translate("MainWindow", "Manual"))
        self.AutoKeepButton.setText(_translate("MainWindow", "Auto Keep"))
        self.AutoScanButton.setText(_translate("MainWindow", "Auto Scan"))
        self.UpButton.setText(_translate("MainWindow", "△"))
        self.UpButton.setShortcut(_translate("MainWindow", "Up"))
        self.ReturnButton.setText(_translate("MainWindow", "Return to 0, 0"))
