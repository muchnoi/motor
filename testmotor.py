#!/usr/bin/env python3
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
import sys, design
from motor import Motor

class Application(QtWidgets.QMainWindow, design.Ui_MainWindow):
  ssa = 'qproperty-alignment: AlignCenter; color: yellow; background-color: darkred'
  ssb = 'qproperty-alignment: AlignCenter; color: yellow; background-color: darkgreen'
  def __init__(self): 
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle('Stepping Motor Control Utility')
    self.timer = QTimer()
    self.M = Motor()
    self.actionQuit.triggered.connect(self.close)
    self.actionSave.triggered.connect(self.M.Save_Data)
    self.initWidgets()
    self.ConnectDevice()
    self.connectWidgets()

  def closeEvent(self, event):
    event.accept()

  def about(self):
    QtWidgets.QMessageBox.about(self, "About Application", "The <b>Application</b> example")

  def initWidgets(self):
    for v in self.M.ioPorts: self.SerialPortBox.addItem('Port: {}'.format(v))
    self.SerialPortBox.setCurrentIndex(self.M.ioPorts.index(self.M.ioPort))
    for v in self.M.ioRates: self.BaudRateBox.addItem('Baud Rate: {}'.format(v))
    self.BaudRateBox.setCurrentIndex(self.M.ioRates.index(self.M.ioRate))
    for v in self.M.Ilimits: 
      self.IMoveBox.addItem('I move = {:3.1f} A'.format(v))
      self.IStopBox.addItem('I stop  = {:3.1f} A'.format(v))
    for v in ['normally closed', 'normally opened']:
      self.LeftTrailerBox.addItem(  'K- ' + v)
      self.CenterTrailerBox.addItem('K0 ' + v)
      self.RightTrailerBox.addItem( 'K+ ' + v)
    self.NphaseBox.addItem('4 - phase motor')
    self.NphaseBox.addItem('8 - phase motor')
    
  def connectWidgets(self):  
    self.SerialPortBox.currentIndexChanged.connect(self.ConnectDevice)
    self.BaudRateBox.currentIndexChanged.connect(  self.ConnectDevice)
    self.DeviceNumberBox.valueChanged.connect(     self.ConnectDevice)
    self.StopButton.clicked.connect(self.Stop)
    self.LeftAccButton.clicked.connect( lambda x: self.Go(True,  -1))
    self.LeftButton.clicked.connect(    lambda x: self.Go(False, -1))
    self.RightButton.clicked.connect(   lambda x: self.Go(False,  1))
    self.RightAccButton.clicked.connect(lambda x: self.Go(True,   1))
    self.CounterButton.clicked.connect(self.CounterReset)
    self.AssignButton.clicked.connect(self.Setup)
    self.IMoveBox.currentIndexChanged.connect(        lambda x: self.Config(reset=True))
    self.IStopBox.currentIndexChanged.connect(        lambda x: self.Config(reset=True))
    self.TStopBox.valueChanged.connect(               lambda x: self.Config(reset=True))
    self.LeftTrailerBox.currentIndexChanged.connect(  lambda x: self.Config(reset=True))
    self.CenterTrailerBox.currentIndexChanged.connect(lambda x: self.Config(reset=True))
    self.RightTrailerBox.currentIndexChanged.connect( lambda x: self.Config(reset=True))
    self.NphaseBox.currentIndexChanged.connect(       lambda x: self.Config(reset=True))
    self.SoftTrailersBox.stateChanged.connect(        lambda x: self.Config(reset=True))
    self.LeaveTrailersBox.stateChanged.connect(       lambda x: self.Config(reset=True))
    self.AccelerateBox.stateChanged.connect(          lambda x: self.Config(reset=True))
    self.VMinBox.valueChanged.connect(                lambda x: self.Speed( reset=True))
    self.VMaxBox.valueChanged.connect(                lambda x: self.Speed( reset=True))
    self.AccelerationBox.valueChanged.connect(        lambda x: self.Speed( reset=True))
    
  def Setup(self):
    self.M.N      = self.DeviceNumberBox.value()
    self.M.ioRate = self.M.ioRates[self.BaudRateBox.currentIndex()]
    self.M.Set_Logical_Address(self.SerialNumberBox.value())
#    self.ConnectDevice()
      
  def Config(self, reset=False):
    if reset:
      IMove =  self.IMoveBox.currentIndex()
      IStop =  self.IStopBox.currentIndex()
      TStop =  self.TStopBox.value()
      CFG   = [self.NphaseBox.currentIndex(), 
               self.LeftTrailerBox.currentIndex(),
               self.RightTrailerBox.currentIndex(),
               self.CenterTrailerBox.currentIndex(),
               self.SoftTrailersBox.isChecked(),
               self.LeaveTrailersBox.isChecked(),
               self.AccelerateBox.isChecked()]
      CFG = CFG[0] | CFG[1]<<2 | CFG[2]<<3 | CFG[3]<<4 | CFG[4]<<5 | CFG[5]<<6 | CFG[6]<<7
      self.M.Set_Device_Config(IMove, IStop, TStop, CFG)
    R = self.M.Get_Device_Config()
    self.IMoveBox.setCurrentIndex(R['MoveI'])
    self.IStopBox.setCurrentIndex(R['StopI'])
    self.TStopBox.setValue(R['StopT'])
    self.NphaseBox.setCurrentIndex(       bool(R['CFG']&0x1))
    self.LeftTrailerBox.setCurrentIndex(  bool(R['CFG']&0x4))
    self.RightTrailerBox.setCurrentIndex( bool(R['CFG']&0x8))
    self.CenterTrailerBox.setCurrentIndex(bool(R['CFG']&0x10))
    self.SoftTrailersBox.setChecked(      bool(R['CFG']&0x20))
    self.LeaveTrailersBox.setChecked(     bool(R['CFG']&0x40))
    self.AccelerateBox.setChecked(        bool(R['CFG']&0x80))

  def Speed(self, reset=False):
    if reset:
      Vmin = self.VMinBox.value() 
      Vmax = self.VMaxBox.value()
      Acc  = self.AccelerationBox.value()
      self.M.Set_Device_Speed(Vmin, Vmax, Acc)
    R = self.M.Get_Device_Speed()
    self.VMinBox.setValue(R['Vmin'])
    self.VMaxBox.setValue(R['Vmax'])
    self.AccelerationBox.setValue(R['Acc'])
      
      
  def CounterReset(self):
    self.M.Set_Abs_Position(0)
    self.CounterButton.setText('Steps counter: 0')

  def Stop(self): self.M.Immediate_Stop()

  def Go(self, acceleration, direction):
    if acceleration: self.M.Go_With_Acc(direction*self.NStepsBox.value())
    else:            self.M.Go_No_Acc(  direction*self.NStepsBox.value())
    self.move = True
  
  def ConnectDevice(self):
    self.move = False
    self.M.N = self.DeviceNumberBox.value()
    self.M.ioPort = self.M.ioPorts[self.SerialPortBox.currentIndex()]
    self.M.ioRate = self.M.ioRates[self.BaudRateBox.currentIndex()]
    R = self.M.Get_Device_Info()
    Version, SN = float(R['Version']), int(R['S/N'])
    if Version and SN:
      self.centralwidget.blockSignals(True)
      self.ConnectionLabel.setStyleSheet(self.ssb)
      self.FirmwareLabel.setStyleSheet(  self.ssb)
      self.ConnectionLabel.setText('Connection: True')
      self.FirmwareLabel.setText('Firmware: {:3.1f}'.format(Version))
      self.SerialNumberBox.setValue(SN)
      self.Config(reset=False)
      self.Speed(reset=False)
      self.M.Get_Abs_Position()
      self.CounterButton.setText('Steps counter: {:d}'.format(self.M.Position))
      self.timer.start(250)
      self.timer.timeout.connect(self.StatusFrame)
      self.centralwidget.blockSignals(False)
    else:
      self.ConnectionLabel.setStyleSheet(self.ssa)
      self.FirmwareLabel.setStyleSheet(  self.ssa)
      self.ConnectionLabel.setText('Connection: False')
      self.FirmwareLabel.setText('Firmware: None')
      self.SerialNumberBox.setValue(0)
      self.timer.stop()

  def StatusFrame(self):
    self.M.Get_Device_Status()
    self.TrailerPlusBox.setChecked(self.M.BS['K+'])
    self.TrailerMinusBox.setChecked(self.M.BS['K-'])
    self.TrailerZeroBox.setChecked(self.M.BS['K0'])
    self.HitTrailerBox.setChecked(self.M.BS['HitK'])
    self.ReadyBox.setChecked(self.M.BS['Ready'])
    self.MoveBox.setChecked(self.M.BS['Move'])
    self.AccurateBox.setChecked(self.M.BS['Accu'])
    if self.M.BS['Ready'] and self.move:
      self.M.Get_Abs_Position()
      self.CounterButton.setText('Steps counter: {:d}'.format(self.M.Position))
      self.move = False
    elif self.M.BS['Move'] and not self.move:
      self.move = True
  
  
  
def main():
  try:
    app    = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    app.exec_()
  except:
    window.closeEvent()
#    window.tabs.__del__()
  print("Good Bye!", file=sys.stderr)

if __name__ == '__main__':  main()  

