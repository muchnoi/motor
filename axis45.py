# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'axis45.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 434)
        MainWindow.setStyleSheet("QWidget{background-color:black;}\n"
"\n"
"\n"
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
"QCheckBox\n"
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
"QGroupBox {\n"
"   background-color: black;\n"
"   color: white;\n"
"   border-style: outset;\n"
"   border-width: 2px;\n"
"   border-radius: 10px;\n"
"   border-color: white;\n"
"   padding: 6px;\n"
"   font-weight: bold;\n"
"}\n"
"QGroupBox::title {  subcontrol-origin: margin;   subcontrol-position: top center;    padding:  0px 5px;  }\n"
"\n"
"\n"
"QPushButton:hover {color: yellow;}\n"
"QLCDNumber {color: lightblue;}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LeftFrame = QtWidgets.QFrame(self.centralwidget)
        self.LeftFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LeftFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LeftFrame.setLineWidth(0)
        self.LeftFrame.setObjectName("LeftFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.LeftFrame)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.LeftUpButt = QtWidgets.QPushButton(self.LeftFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftUpButt.sizePolicy().hasHeightForWidth())
        self.LeftUpButt.setSizePolicy(sizePolicy)
        self.LeftUpButt.setMinimumSize(QtCore.QSize(120, 120))
        self.LeftUpButt.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.LeftUpButt.setFont(font)
        self.LeftUpButt.setObjectName("LeftUpButt")
        self.gridLayout.addWidget(self.LeftUpButt, 0, 0, 1, 1)
        self.UpButt = QtWidgets.QPushButton(self.LeftFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UpButt.sizePolicy().hasHeightForWidth())
        self.UpButt.setSizePolicy(sizePolicy)
        self.UpButt.setMinimumSize(QtCore.QSize(120, 120))
        self.UpButt.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.UpButt.setFont(font)
        self.UpButt.setObjectName("UpButt")
        self.gridLayout.addWidget(self.UpButt, 0, 1, 1, 1)
        self.RightUpButt = QtWidgets.QPushButton(self.LeftFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightUpButt.sizePolicy().hasHeightForWidth())
        self.RightUpButt.setSizePolicy(sizePolicy)
        self.RightUpButt.setMinimumSize(QtCore.QSize(120, 120))
        self.RightUpButt.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.RightUpButt.setFont(font)
        self.RightUpButt.setStyleSheet("")
        self.RightUpButt.setObjectName("RightUpButt")
        self.gridLayout.addWidget(self.RightUpButt, 0, 2, 1, 1)
        self.LeftButt = QtWidgets.QPushButton(self.LeftFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftButt.sizePolicy().hasHeightForWidth())
        self.LeftButt.setSizePolicy(sizePolicy)
        self.LeftButt.setMinimumSize(QtCore.QSize(120, 120))
        self.LeftButt.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.LeftButt.setFont(font)
        self.LeftButt.setObjectName("LeftButt")
        self.gridLayout.addWidget(self.LeftButt, 1, 0, 1, 1)
        self.CountersFrame = QtWidgets.QFrame(self.LeftFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CountersFrame.sizePolicy().hasHeightForWidth())
        self.CountersFrame.setSizePolicy(sizePolicy)
        self.CountersFrame.setMinimumSize(QtCore.QSize(120, 120))
        self.CountersFrame.setMaximumSize(QtCore.QSize(1000, 1000))
        self.CountersFrame.setStyleSheet("QFrame#CountersFrame{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: white;\n"
"    color: white; \n"
"    background-color:black;\n"
"}")
        self.CountersFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.CountersFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CountersFrame.setObjectName("CountersFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.CountersFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(self.CountersFrame)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.YlcdNumber = QtWidgets.QLCDNumber(self.CountersFrame)
        self.YlcdNumber.setStyleSheet("")
        self.YlcdNumber.setDigitCount(6)
        self.YlcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.YlcdNumber.setObjectName("YlcdNumber")
        self.verticalLayout.addWidget(self.YlcdNumber)
        self.label_2 = QtWidgets.QLabel(self.CountersFrame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.XlcdNumber = QtWidgets.QLCDNumber(self.CountersFrame)
        self.XlcdNumber.setDigitCount(6)
        self.XlcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.XlcdNumber.setObjectName("XlcdNumber")
        self.verticalLayout.addWidget(self.XlcdNumber)
        self.gridLayout.addWidget(self.CountersFrame, 1, 1, 1, 1)
        self.RightButt = QtWidgets.QPushButton(self.LeftFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightButt.sizePolicy().hasHeightForWidth())
        self.RightButt.setSizePolicy(sizePolicy)
        self.RightButt.setMinimumSize(QtCore.QSize(120, 120))
        self.RightButt.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.RightButt.setFont(font)
        self.RightButt.setObjectName("RightButt")
        self.gridLayout.addWidget(self.RightButt, 1, 2, 1, 1)
        self.LeftDownButt = QtWidgets.QPushButton(self.LeftFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftDownButt.sizePolicy().hasHeightForWidth())
        self.LeftDownButt.setSizePolicy(sizePolicy)
        self.LeftDownButt.setMinimumSize(QtCore.QSize(120, 120))
        self.LeftDownButt.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.LeftDownButt.setFont(font)
        self.LeftDownButt.setObjectName("LeftDownButt")
        self.gridLayout.addWidget(self.LeftDownButt, 2, 0, 1, 1)
        self.DownButt = QtWidgets.QPushButton(self.LeftFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DownButt.sizePolicy().hasHeightForWidth())
        self.DownButt.setSizePolicy(sizePolicy)
        self.DownButt.setMinimumSize(QtCore.QSize(120, 120))
        self.DownButt.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.DownButt.setFont(font)
        self.DownButt.setObjectName("DownButt")
        self.gridLayout.addWidget(self.DownButt, 2, 1, 1, 1)
        self.RightDownButt = QtWidgets.QPushButton(self.LeftFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightDownButt.sizePolicy().hasHeightForWidth())
        self.RightDownButt.setSizePolicy(sizePolicy)
        self.RightDownButt.setMinimumSize(QtCore.QSize(120, 120))
        self.RightDownButt.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.RightDownButt.setFont(font)
        self.RightDownButt.setObjectName("RightDownButt")
        self.gridLayout.addWidget(self.RightDownButt, 2, 2, 1, 1)
        self.horizontalLayout.addWidget(self.LeftFrame)
        self.RightFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightFrame.sizePolicy().hasHeightForWidth())
        self.RightFrame.setSizePolicy(sizePolicy)
        self.RightFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.RightFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.RightFrame.setObjectName("RightFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.RightFrame)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.StepsGroup = QtWidgets.QGroupBox(self.RightFrame)
        self.StepsGroup.setObjectName("StepsGroup")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.StepsGroup)
        self.verticalLayout_3.setContentsMargins(-1, 11, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.StepsBox = QtWidgets.QSpinBox(self.StepsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StepsBox.sizePolicy().hasHeightForWidth())
        self.StepsBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.StepsBox.setFont(font)
        self.StepsBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.StepsBox.setMinimum(1)
        self.StepsBox.setMaximum(10000)
        self.StepsBox.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.StepsBox.setProperty("value", 57)
        self.StepsBox.setObjectName("StepsBox")
        self.verticalLayout_3.addWidget(self.StepsBox)
        self.verticalLayout_2.addWidget(self.StepsGroup)
        self.ResetButt = QtWidgets.QPushButton(self.RightFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResetButt.sizePolicy().hasHeightForWidth())
        self.ResetButt.setSizePolicy(sizePolicy)
        self.ResetButt.setObjectName("ResetButt")
        self.verticalLayout_2.addWidget(self.ResetButt)
        self.ModeGroup = QtWidgets.QGroupBox(self.RightFrame)
        self.ModeGroup.setObjectName("ModeGroup")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.ModeGroup)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.LaserON = QtWidgets.QRadioButton(self.ModeGroup)
        self.LaserON.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.LaserON.setObjectName("LaserON")
        self.verticalLayout_4.addWidget(self.LaserON)
        self.LaserOFF = QtWidgets.QRadioButton(self.ModeGroup)
        self.LaserOFF.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.LaserOFF.setObjectName("LaserOFF")
        self.verticalLayout_4.addWidget(self.LaserOFF)
        self.AutoMode = QtWidgets.QCheckBox(self.ModeGroup)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AutoMode.setFont(font)
        self.AutoMode.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.AutoMode.setObjectName("AutoMode")
        self.verticalLayout_4.addWidget(self.AutoMode)
        self.verticalLayout_2.addWidget(self.ModeGroup)
        self.ReturnButt = QtWidgets.QPushButton(self.RightFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ReturnButt.sizePolicy().hasHeightForWidth())
        self.ReturnButt.setSizePolicy(sizePolicy)
        self.ReturnButt.setObjectName("ReturnButt")
        self.verticalLayout_2.addWidget(self.ReturnButt)
        self.horizontalLayout.addWidget(self.RightFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LeftUpButt.setText(_translate("MainWindow", "⬉"))
        self.UpButt.setText(_translate("MainWindow", "⬆"))
        self.UpButt.setShortcut(_translate("MainWindow", "Up"))
        self.RightUpButt.setText(_translate("MainWindow", "⬈"))
        self.LeftButt.setText(_translate("MainWindow", "⬅"))
        self.LeftButt.setShortcut(_translate("MainWindow", "Left"))
        self.label_1.setText(_translate("MainWindow", "Y, [μm]"))
        self.label_2.setText(_translate("MainWindow", "X, [μm]"))
        self.RightButt.setText(_translate("MainWindow", "➡"))
        self.RightButt.setShortcut(_translate("MainWindow", "Right"))
        self.LeftDownButt.setText(_translate("MainWindow", "⬋"))
        self.DownButt.setText(_translate("MainWindow", "⬇"))
        self.DownButt.setShortcut(_translate("MainWindow", "Down"))
        self.RightDownButt.setText(_translate("MainWindow", "⬊"))
        self.StepsGroup.setTitle(_translate("MainWindow", "Steps / Click"))
        self.ResetButt.setText(_translate("MainWindow", "Reset Counters"))
        self.ModeGroup.setTitle(_translate("MainWindow", "Laser"))
        self.LaserON.setText(_translate("MainWindow", "ON"))
        self.LaserOFF.setText(_translate("MainWindow", "OFF"))
        self.AutoMode.setText(_translate("MainWindow", "Auto"))
        self.ReturnButt.setText(_translate("MainWindow", "Return to 0, 0"))
