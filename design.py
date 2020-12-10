# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 457)
        MainWindow.setStyleSheet("QGroupBox { border: 1px solid grey;   border-radius: 10px;   font-weight: bold; font-size: 11pt; padding:8px; margin:8px; background-color: #F0F0F0;}\n"
"QGroupBox::title {  subcontrol-origin: margin;   subcontrol-position: top center;    padding:  0 5px;  }\n"
"QSpinBox {             background-color: #FFFFFF; }\n"
"QDoubleSpinBox {background-color: #FFFFFF;} \n"
"QGroupBox#ConnectionGroupBox { border: 1px solid darkred; color: darkred;}\n"
"QGroupBox#ConfigurationGroupBox { border: 1px solid darkgreen; color: darkgreen; }\n"
"QGroupBox#MovementGroupBox { border: 1px solid darkblue; color: darkblue;}\n"
"QGroupBox#StatusGroupBox { border: 1px solid darkred; color: darkred;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ConnectionGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConnectionGroupBox.sizePolicy().hasHeightForWidth())
        self.ConnectionGroupBox.setSizePolicy(sizePolicy)
        self.ConnectionGroupBox.setObjectName("ConnectionGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ConnectionGroupBox)
        self.horizontalLayout.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DeviceNumberBox = QtWidgets.QSpinBox(self.ConnectionGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DeviceNumberBox.sizePolicy().hasHeightForWidth())
        self.DeviceNumberBox.setSizePolicy(sizePolicy)
        self.DeviceNumberBox.setMinimumSize(QtCore.QSize(120, 0))
        self.DeviceNumberBox.setMaximumSize(QtCore.QSize(120, 16777215))
        self.DeviceNumberBox.setAccelerated(False)
        self.DeviceNumberBox.setProperty("value", 1)
        self.DeviceNumberBox.setObjectName("DeviceNumberBox")
        self.horizontalLayout.addWidget(self.DeviceNumberBox)
        self.SerialPortBox = QtWidgets.QComboBox(self.ConnectionGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SerialPortBox.sizePolicy().hasHeightForWidth())
        self.SerialPortBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.SerialPortBox.setFont(font)
        self.SerialPortBox.setObjectName("SerialPortBox")
        self.horizontalLayout.addWidget(self.SerialPortBox)
        self.BaudRateBox = QtWidgets.QComboBox(self.ConnectionGroupBox)
        self.BaudRateBox.setObjectName("BaudRateBox")
        self.horizontalLayout.addWidget(self.BaudRateBox)
        self.SerialNumberBox = QtWidgets.QSpinBox(self.ConnectionGroupBox)
        self.SerialNumberBox.setMinimumSize(QtCore.QSize(100, 0))
        self.SerialNumberBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.SerialNumberBox.setMinimum(0)
        self.SerialNumberBox.setMaximum(1000)
        self.SerialNumberBox.setProperty("value", 0)
        self.SerialNumberBox.setObjectName("SerialNumberBox")
        self.horizontalLayout.addWidget(self.SerialNumberBox)
        self.AssignButton = QtWidgets.QPushButton(self.ConnectionGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AssignButton.sizePolicy().hasHeightForWidth())
        self.AssignButton.setSizePolicy(sizePolicy)
        self.AssignButton.setMinimumSize(QtCore.QSize(0, 0))
        self.AssignButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.AssignButton.setObjectName("AssignButton")
        self.horizontalLayout.addWidget(self.AssignButton)
        self.verticalLayout.addWidget(self.ConnectionGroupBox)
        self.ConfigurationGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ConfigurationGroupBox.setObjectName("ConfigurationGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.ConfigurationGroupBox)
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.DebugBox = QtWidgets.QCheckBox(self.ConfigurationGroupBox)
        self.DebugBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.DebugBox.setObjectName("DebugBox")
        self.gridLayout.addWidget(self.DebugBox, 0, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.NphaseBox = QtWidgets.QComboBox(self.ConfigurationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NphaseBox.sizePolicy().hasHeightForWidth())
        self.NphaseBox.setSizePolicy(sizePolicy)
        self.NphaseBox.setMinimumSize(QtCore.QSize(150, 0))
        self.NphaseBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.NphaseBox.setObjectName("NphaseBox")
        self.gridLayout.addWidget(self.NphaseBox, 1, 4, 1, 1)
        self.VMinBox = QtWidgets.QSpinBox(self.ConfigurationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VMinBox.sizePolicy().hasHeightForWidth())
        self.VMinBox.setSizePolicy(sizePolicy)
        self.VMinBox.setMinimum(32)
        self.VMinBox.setMaximum(12000)
        self.VMinBox.setSingleStep(100)
        self.VMinBox.setProperty("value", 100)
        self.VMinBox.setObjectName("VMinBox")
        self.gridLayout.addWidget(self.VMinBox, 0, 1, 1, 1)
        self.AccelerationBox = QtWidgets.QSpinBox(self.ConfigurationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccelerationBox.sizePolicy().hasHeightForWidth())
        self.AccelerationBox.setSizePolicy(sizePolicy)
        self.AccelerationBox.setMinimumSize(QtCore.QSize(160, 0))
        self.AccelerationBox.setMinimum(32)
        self.AccelerationBox.setMaximum(65535)
        self.AccelerationBox.setSingleStep(100)
        self.AccelerationBox.setProperty("value", 100)
        self.AccelerationBox.setObjectName("AccelerationBox")
        self.gridLayout.addWidget(self.AccelerationBox, 0, 3, 1, 1)
        self.CenterTrailerBox = QtWidgets.QComboBox(self.ConfigurationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CenterTrailerBox.sizePolicy().hasHeightForWidth())
        self.CenterTrailerBox.setSizePolicy(sizePolicy)
        self.CenterTrailerBox.setObjectName("CenterTrailerBox")
        self.gridLayout.addWidget(self.CenterTrailerBox, 1, 2, 1, 1)
        self.LeftTrailerBox = QtWidgets.QComboBox(self.ConfigurationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftTrailerBox.sizePolicy().hasHeightForWidth())
        self.LeftTrailerBox.setSizePolicy(sizePolicy)
        self.LeftTrailerBox.setObjectName("LeftTrailerBox")
        self.gridLayout.addWidget(self.LeftTrailerBox, 1, 1, 1, 1)
        self.AccelerateBox = QtWidgets.QCheckBox(self.ConfigurationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccelerateBox.sizePolicy().hasHeightForWidth())
        self.AccelerateBox.setSizePolicy(sizePolicy)
        self.AccelerateBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.AccelerateBox.setObjectName("AccelerateBox")
        self.gridLayout.addWidget(self.AccelerateBox, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.IStopBox = QtWidgets.QComboBox(self.ConfigurationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IStopBox.sizePolicy().hasHeightForWidth())
        self.IStopBox.setSizePolicy(sizePolicy)
        self.IStopBox.setObjectName("IStopBox")
        self.gridLayout.addWidget(self.IStopBox, 2, 0, 1, 1)
        self.IMoveBox = QtWidgets.QComboBox(self.ConfigurationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IMoveBox.sizePolicy().hasHeightForWidth())
        self.IMoveBox.setSizePolicy(sizePolicy)
        self.IMoveBox.setMinimumSize(QtCore.QSize(120, 0))
        self.IMoveBox.setMaximumSize(QtCore.QSize(120, 16777215))
        self.IMoveBox.setObjectName("IMoveBox")
        self.gridLayout.addWidget(self.IMoveBox, 1, 0, 1, 1)
        self.RightTrailerBox = QtWidgets.QComboBox(self.ConfigurationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightTrailerBox.sizePolicy().hasHeightForWidth())
        self.RightTrailerBox.setSizePolicy(sizePolicy)
        self.RightTrailerBox.setObjectName("RightTrailerBox")
        self.gridLayout.addWidget(self.RightTrailerBox, 1, 3, 1, 1)
        self.FirmwareLabel = QtWidgets.QLabel(self.ConfigurationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FirmwareLabel.sizePolicy().hasHeightForWidth())
        self.FirmwareLabel.setSizePolicy(sizePolicy)
        self.FirmwareLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.FirmwareLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.FirmwareLabel.setObjectName("FirmwareLabel")
        self.gridLayout.addWidget(self.FirmwareLabel, 0, 0, 1, 1)
        self.LeaveTrailersBox = QtWidgets.QCheckBox(self.ConfigurationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeaveTrailersBox.sizePolicy().hasHeightForWidth())
        self.LeaveTrailersBox.setSizePolicy(sizePolicy)
        self.LeaveTrailersBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.LeaveTrailersBox.setObjectName("LeaveTrailersBox")
        self.gridLayout.addWidget(self.LeaveTrailersBox, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.SoftTrailersBox = QtWidgets.QCheckBox(self.ConfigurationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SoftTrailersBox.sizePolicy().hasHeightForWidth())
        self.SoftTrailersBox.setSizePolicy(sizePolicy)
        self.SoftTrailersBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.SoftTrailersBox.setObjectName("SoftTrailersBox")
        self.gridLayout.addWidget(self.SoftTrailersBox, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.TStopBox = QtWidgets.QSpinBox(self.ConfigurationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TStopBox.sizePolicy().hasHeightForWidth())
        self.TStopBox.setSizePolicy(sizePolicy)
        self.TStopBox.setMaximum(255)
        self.TStopBox.setProperty("value", 1)
        self.TStopBox.setObjectName("TStopBox")
        self.gridLayout.addWidget(self.TStopBox, 2, 4, 1, 1)
        self.VMaxBox = QtWidgets.QSpinBox(self.ConfigurationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VMaxBox.sizePolicy().hasHeightForWidth())
        self.VMaxBox.setSizePolicy(sizePolicy)
        self.VMaxBox.setMinimum(32)
        self.VMaxBox.setMaximum(12000)
        self.VMaxBox.setSingleStep(100)
        self.VMaxBox.setProperty("value", 1000)
        self.VMaxBox.setObjectName("VMaxBox")
        self.gridLayout.addWidget(self.VMaxBox, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.ConfigurationGroupBox)
        self.MovementGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.MovementGroupBox.setObjectName("MovementGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.MovementGroupBox)
        self.horizontalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.NStepsBox = QtWidgets.QSpinBox(self.MovementGroupBox)
        self.NStepsBox.setSuffix("")
        self.NStepsBox.setMinimum(1)
        self.NStepsBox.setMaximum(1000000)
        self.NStepsBox.setProperty("value", 100)
        self.NStepsBox.setObjectName("NStepsBox")
        self.horizontalLayout_2.addWidget(self.NStepsBox)
        self.LeftAccButton = QtWidgets.QPushButton(self.MovementGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftAccButton.sizePolicy().hasHeightForWidth())
        self.LeftAccButton.setSizePolicy(sizePolicy)
        self.LeftAccButton.setMinimumSize(QtCore.QSize(20, 40))
        self.LeftAccButton.setMaximumSize(QtCore.QSize(40, 40))
        self.LeftAccButton.setObjectName("LeftAccButton")
        self.horizontalLayout_2.addWidget(self.LeftAccButton)
        self.LeftButton = QtWidgets.QPushButton(self.MovementGroupBox)
        self.LeftButton.setMinimumSize(QtCore.QSize(20, 40))
        self.LeftButton.setMaximumSize(QtCore.QSize(40, 40))
        self.LeftButton.setObjectName("LeftButton")
        self.horizontalLayout_2.addWidget(self.LeftButton)
        self.StopButton = QtWidgets.QPushButton(self.MovementGroupBox)
        self.StopButton.setMinimumSize(QtCore.QSize(0, 40))
        self.StopButton.setMaximumSize(QtCore.QSize(60, 40))
        self.StopButton.setObjectName("StopButton")
        self.horizontalLayout_2.addWidget(self.StopButton)
        self.RightButton = QtWidgets.QPushButton(self.MovementGroupBox)
        self.RightButton.setMinimumSize(QtCore.QSize(20, 40))
        self.RightButton.setMaximumSize(QtCore.QSize(40, 40))
        self.RightButton.setObjectName("RightButton")
        self.horizontalLayout_2.addWidget(self.RightButton)
        self.RightAccButton = QtWidgets.QPushButton(self.MovementGroupBox)
        self.RightAccButton.setMinimumSize(QtCore.QSize(20, 40))
        self.RightAccButton.setMaximumSize(QtCore.QSize(40, 40))
        self.RightAccButton.setObjectName("RightAccButton")
        self.horizontalLayout_2.addWidget(self.RightAccButton)
        self.CounterButton = QtWidgets.QPushButton(self.MovementGroupBox)
        self.CounterButton.setObjectName("CounterButton")
        self.horizontalLayout_2.addWidget(self.CounterButton)
        self.verticalLayout.addWidget(self.MovementGroupBox)
        self.StatusGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.StatusGroupBox.setObjectName("StatusGroupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.StatusGroupBox)
        self.horizontalLayout_3.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.TrailerMinusBox = QtWidgets.QCheckBox(self.StatusGroupBox)
        self.TrailerMinusBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.TrailerMinusBox.setStyleSheet("")
        self.TrailerMinusBox.setObjectName("TrailerMinusBox")
        self.horizontalLayout_3.addWidget(self.TrailerMinusBox)
        self.TrailerZeroBox = QtWidgets.QCheckBox(self.StatusGroupBox)
        self.TrailerZeroBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.TrailerZeroBox.setStyleSheet("")
        self.TrailerZeroBox.setObjectName("TrailerZeroBox")
        self.horizontalLayout_3.addWidget(self.TrailerZeroBox)
        self.TrailerPlusBox = QtWidgets.QCheckBox(self.StatusGroupBox)
        self.TrailerPlusBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.TrailerPlusBox.setStyleSheet("")
        self.TrailerPlusBox.setObjectName("TrailerPlusBox")
        self.horizontalLayout_3.addWidget(self.TrailerPlusBox)
        self.HitTrailerBox = QtWidgets.QCheckBox(self.StatusGroupBox)
        self.HitTrailerBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.HitTrailerBox.setStyleSheet("")
        self.HitTrailerBox.setObjectName("HitTrailerBox")
        self.horizontalLayout_3.addWidget(self.HitTrailerBox)
        self.ReadyBox = QtWidgets.QCheckBox(self.StatusGroupBox)
        self.ReadyBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ReadyBox.setStyleSheet("")
        self.ReadyBox.setObjectName("ReadyBox")
        self.horizontalLayout_3.addWidget(self.ReadyBox)
        self.MoveBox = QtWidgets.QCheckBox(self.StatusGroupBox)
        self.MoveBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.MoveBox.setStyleSheet("")
        self.MoveBox.setObjectName("MoveBox")
        self.horizontalLayout_3.addWidget(self.MoveBox)
        self.AccurateBox = QtWidgets.QCheckBox(self.StatusGroupBox)
        self.AccurateBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.AccurateBox.setStyleSheet("")
        self.AccurateBox.setObjectName("AccurateBox")
        self.horizontalLayout_3.addWidget(self.AccurateBox)
        self.verticalLayout.addWidget(self.StatusGroupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.SerialPortBox, self.BaudRateBox)
        MainWindow.setTabOrder(self.BaudRateBox, self.SerialNumberBox)
        MainWindow.setTabOrder(self.SerialNumberBox, self.AssignButton)
        MainWindow.setTabOrder(self.AssignButton, self.VMinBox)
        MainWindow.setTabOrder(self.VMinBox, self.VMaxBox)
        MainWindow.setTabOrder(self.VMaxBox, self.AccelerationBox)
        MainWindow.setTabOrder(self.AccelerationBox, self.IMoveBox)
        MainWindow.setTabOrder(self.IMoveBox, self.LeftTrailerBox)
        MainWindow.setTabOrder(self.LeftTrailerBox, self.CenterTrailerBox)
        MainWindow.setTabOrder(self.CenterTrailerBox, self.RightTrailerBox)
        MainWindow.setTabOrder(self.RightTrailerBox, self.NphaseBox)
        MainWindow.setTabOrder(self.NphaseBox, self.IStopBox)
        MainWindow.setTabOrder(self.IStopBox, self.SoftTrailersBox)
        MainWindow.setTabOrder(self.SoftTrailersBox, self.LeaveTrailersBox)
        MainWindow.setTabOrder(self.LeaveTrailersBox, self.AccelerateBox)
        MainWindow.setTabOrder(self.AccelerateBox, self.TStopBox)
        MainWindow.setTabOrder(self.TStopBox, self.NStepsBox)
        MainWindow.setTabOrder(self.NStepsBox, self.LeftAccButton)
        MainWindow.setTabOrder(self.LeftAccButton, self.LeftButton)
        MainWindow.setTabOrder(self.LeftButton, self.StopButton)
        MainWindow.setTabOrder(self.StopButton, self.RightButton)
        MainWindow.setTabOrder(self.RightButton, self.RightAccButton)
        MainWindow.setTabOrder(self.RightAccButton, self.CounterButton)
        MainWindow.setTabOrder(self.CounterButton, self.TrailerMinusBox)
        MainWindow.setTabOrder(self.TrailerMinusBox, self.TrailerZeroBox)
        MainWindow.setTabOrder(self.TrailerZeroBox, self.TrailerPlusBox)
        MainWindow.setTabOrder(self.TrailerPlusBox, self.HitTrailerBox)
        MainWindow.setTabOrder(self.HitTrailerBox, self.ReadyBox)
        MainWindow.setTabOrder(self.ReadyBox, self.MoveBox)
        MainWindow.setTabOrder(self.MoveBox, self.AccurateBox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ConnectionGroupBox.setTitle(_translate("MainWindow", "Connection"))
        self.DeviceNumberBox.setPrefix(_translate("MainWindow", "Device: "))
        self.SerialNumberBox.setPrefix(_translate("MainWindow", "S/N: "))
        self.AssignButton.setText(_translate("MainWindow", "Assign S/N and BaudRate"))
        self.ConfigurationGroupBox.setTitle(_translate("MainWindow", "Configuration"))
        self.DebugBox.setText(_translate("MainWindow", "Debug Mode"))
        self.VMinBox.setSuffix(_translate("MainWindow", " [s⁻¹]"))
        self.VMinBox.setPrefix(_translate("MainWindow", "V min: "))
        self.AccelerationBox.setSuffix(_translate("MainWindow", " [s⁻²]"))
        self.AccelerationBox.setPrefix(_translate("MainWindow", "Accelerate: "))
        self.AccelerateBox.setText(_translate("MainWindow", "Accelerate on Leave:"))
        self.FirmwareLabel.setText(_translate("MainWindow", "Firmware: None"))
        self.LeaveTrailersBox.setText(_translate("MainWindow", "Leave Trailers:"))
        self.SoftTrailersBox.setText(_translate("MainWindow", "Soft Trailers:"))
        self.TStopBox.setSuffix(_translate("MainWindow", "/30 [s]"))
        self.TStopBox.setPrefix(_translate("MainWindow", "Stop time: "))
        self.VMaxBox.setSuffix(_translate("MainWindow", " [s⁻¹]"))
        self.VMaxBox.setPrefix(_translate("MainWindow", "V max: "))
        self.MovementGroupBox.setTitle(_translate("MainWindow", "Movement"))
        self.NStepsBox.setPrefix(_translate("MainWindow", "Number of steps: "))
        self.LeftAccButton.setText(_translate("MainWindow", "<<"))
        self.LeftButton.setText(_translate("MainWindow", "<"))
        self.StopButton.setText(_translate("MainWindow", "STOP"))
        self.RightButton.setText(_translate("MainWindow", ">"))
        self.RightAccButton.setText(_translate("MainWindow", ">>"))
        self.CounterButton.setText(_translate("MainWindow", "PushButton"))
        self.StatusGroupBox.setTitle(_translate("MainWindow", "Status"))
        self.TrailerMinusBox.setText(_translate("MainWindow", "Trailer -"))
        self.TrailerZeroBox.setText(_translate("MainWindow", "Trailer  0"))
        self.TrailerPlusBox.setText(_translate("MainWindow", "Trailer +"))
        self.HitTrailerBox.setText(_translate("MainWindow", "Hit Trailer"))
        self.ReadyBox.setText(_translate("MainWindow", "Ready"))
        self.MoveBox.setText(_translate("MainWindow", "Move"))
        self.AccurateBox.setText(_translate("MainWindow", "Accurate"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSave.setText(_translate("MainWindow", "Save Settings to Device"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
