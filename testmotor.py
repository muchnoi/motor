#!/usr/bin/env python3
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
import sys, design, time
from motor import Motor

class Application(QtWidgets.QMainWindow, design.Ui_MainWindow):
  ssa = 'qproperty-alignment: AlignCenter; color: yellow; background-color: darkred'
  ssb = 'qproperty-alignment: AlignCenter; color: yellow; background-color: darkgreen'
  def __init__(self): 
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle('Stepping Motor Control Utility')
    self.setWindowIcon(QIcon('test.png'))
    self.M = Motor(DEBUG=True)
    self.actionQuit.triggered.connect(self.close)
    self.actionSave.triggered.connect(self.M.Save_Data)
    self.initWidgets()
    self.ConnectDevice()

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
      self.IStopBox.addItem('I stop = {:3.1f} A'.format(v))
    for v in ['normally closed', 'normally opened']:
      self.LeftTrailerBox.addItem(  'K- ' + v)
      self.CenterTrailerBox.addItem('K0 ' + v)
      self.RightTrailerBox.addItem( 'K+ ' + v)
    self.NphaseBox.addItem('4 - phase motor')
    self.NphaseBox.addItem('8 - phase motor')
    self.DebugBox.setChecked(True)
    self.timer = QTimer(); self.timer.setSingleShot(True); self.timer.setInterval(250)
    self.delay = QTimer(); self.delay.setSingleShot(True); self.delay.setInterval(100)
    self.DebugBox.clicked.connect(                    self.DebugMode)
    self.delay.timeout.connect(                       self.DelayedConnectDevice)
    self.timer.timeout.connect(                       self.StatusFrame)
    self.DeviceNumberBox.valueChanged.connect(        self.ConnectDevice)
    self.SerialPortBox.currentIndexChanged.connect(   self.ConnectDevice)
    self.BaudRateBox.currentIndexChanged.connect(     self.ConnectDevice)
    self.StopButton.clicked.connect(                  self.Stop)
    self.LeftAccButton.clicked.connect(     lambda x: self.Go(True,  -1))
    self.LeftButton.clicked.connect(        lambda x: self.Go(False, -1))
    self.RightButton.clicked.connect(       lambda x: self.Go(False,  1))
    self.RightAccButton.clicked.connect(    lambda x: self.Go(True,   1))
    self.CounterButton.clicked.connect(               self.CounterReset)
    self.AssignButton.clicked.connect(                self.Setup)
    self.IMoveBox.currentIndexChanged.connect(        self.ConfigDevice)
    self.IStopBox.currentIndexChanged.connect(        self.ConfigDevice)
    self.TStopBox.valueChanged.connect(               self.ConfigDevice)
    self.LeftTrailerBox.currentIndexChanged.connect(  self.ConfigDevice)
    self.CenterTrailerBox.currentIndexChanged.connect(self.ConfigDevice)
    self.RightTrailerBox.currentIndexChanged.connect( self.ConfigDevice)
    self.NphaseBox.currentIndexChanged.connect(       self.ConfigDevice)
    self.SoftTrailersBox.stateChanged.connect(        self.ConfigDevice)
    self.LeaveTrailersBox.stateChanged.connect(       self.ConfigDevice)
    self.AccelerateBox.stateChanged.connect(          self.ConfigDevice)
    self.VMinBox.valueChanged.connect(                self.Speed)
    self.VMaxBox.valueChanged.connect(                self.Speed)
    self.AcceBox.valueChanged.connect(                self.Speed)

  def DebugMode(self):
    if self.DebugBox.isChecked(): self.M.DEBUG = True
    else:                         self.M.DEBUG = False
  
  def Setup(self):
    self.M.N      = self.DeviceNumberBox.value()
    self.M.ioRate = self.M.ioRates[self.BaudRateBox.currentIndex()]
    self.M.Set_Logical_Address(self.SerialNumberBox.value())
    self.ConnectDevice()

  def ConnectDevice(self):
    self.delay.start()
    
  def DelayedConnectDevice(self):
    self.M.N = self.DeviceNumberBox.value()
    self.M.ioPort = self.M.ioPorts[self.SerialPortBox.currentIndex()]
    self.M.ioRate = self.M.ioRates[self.BaudRateBox.currentIndex()]
    R = self.M.Get_Device_Info()
    Version, SN = float(R['Version']), int(R['S/N'])
    if Version and SN:
      self.FirmwareLabel.setStyleSheet(  self.ssb)
      self.FirmwareLabel.setText('Firmware: {:3.1f}'.format(Version))
      self.SerialNumberBox.setValue(SN)
      self.ConfigDevice(0, reset=False)
      self.Speed(0, reset=False)
      self.M.Get_Abs_Position()
      self.StatusFrame()
#      self.M.Write_User_Data('motor on the window')
#      print(self.M.Read_User_Data())
    else:
      self.FirmwareLabel.setStyleSheet(  self.ssa)
      self.FirmwareLabel.setText('Firmware: None')
      self.SerialNumberBox.setValue(0)
      self.CounterButton.setText('Steps counter: None')
      
  def ConfigDevice(self, junk, reset=True):
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
    self.assignIndex( self.IMoveBox, R['MoveI'])
    self.assignIndex( self.IStopBox, R['StopI'])
    self.assignValue( self.TStopBox, R['StopT'])
    self.assignIndex( self.NphaseBox,        bool(R['CFG']&0x01))
    self.assignIndex( self.LeftTrailerBox,   bool(R['CFG']&0x04))
    self.assignIndex( self.RightTrailerBox,  bool(R['CFG']&0x08))
    self.assignIndex( self.CenterTrailerBox, bool(R['CFG']&0x10))
    self.assignStatus(self.SoftTrailersBox,  bool(R['CFG']&0x20))
    self.assignStatus(self.LeaveTrailersBox, bool(R['CFG']&0x40))
    self.assignStatus(self.AccelerateBox,    bool(R['CFG']&0x80))

  def Speed(self, junk, reset=False):
    if reset:
      self.M.Set_Device_Speed(self.VMinBox.value(), self.VMaxBox.value(), self.AcceBox.value())
    R = self.M.Get_Device_Speed()
    self.assignValue(self.VMinBox, R['Vmin']);  self.vmin = 1.e-3*R['Vmin'] # steps/ms
    self.assignValue(self.VMaxBox, R['Vmax']);  self.vmax = 1.e-3*R['Vmax'] # steps/ms
    self.assignValue(self.AcceBox, R['Acc'] );  self.acce = 1.e-6*R['Acc' ] # steps/ms^2
      
  def CounterReset(self):
    self.M.Set_Abs_Position(0)
    self.StatusFrame()

  def Stop(self): 
    self.M.Immediate_Stop()
    self.StatusFrame()

  def Go(self, acceleration, direction):
    if acceleration: 
      self.M.Go_With_Acc(direction*self.NStepsBox.value())
      self.tacc = (self.vmax-self.vmin)/self.acce # acceleration time in ms
    else:            
      self.M.Go_No_Acc(  direction*self.NStepsBox.value())
      self.tacc = 0.0                             # acceleration time in ms
    self.tstart = time.time()
    self.side = direction
    self.StatusFrame()
  
  def StatusFrame(self):
    self.M.Get_Device_Status()
    self.TrailerPlusBox.setChecked(self.M.BS['K+'])
    self.TrailerMinusBox.setChecked(self.M.BS['K-'])
    self.TrailerZeroBox.setChecked(self.M.BS['K0'])
    self.HitTrailerBox.setChecked(self.M.BS['HitK'])
    self.ReadyBox.setChecked(self.M.BS['Ready'])
    self.MoveBox.setChecked(self.M.BS['Move'])
    self.AccurateBox.setChecked(self.M.BS['Accu'])
    if self.M.BS['Ready']:
      self.M.Get_Abs_Position()
      self.CounterButton.setText('Steps counter: {:d}'.format(self.M.Position))
    else:
      t = 1000*(time.time()-self.tstart) # time from start [ms]
      if t<self.tacc: P = self.M.Position + int(self.side*(self.vmin*t + self.acce*t*t))
      else:           P = self.M.Position + int(self.side*(self.vmin*t + self.acce*self.tacc*t))
      self.CounterButton.setText('Steps counter: {:d}'.format(P))
      self.timer.start()

  def assignIndex(self, widget, index):
    widget.blockSignals(True);  widget.setCurrentIndex(index);  widget.blockSignals(False)
    
  def assignValue(self, widget, value):
    widget.blockSignals(True);  widget.setValue(value);         widget.blockSignals(False)

  def assignStatus(self, widget, status):
    widget.blockSignals(True);  widget.setChecked(status);      widget.blockSignals(False)

def main():
  try:
    app    = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    app.exec_()
  except:
    window.closeEvent()
  print("Good Bye!", file=sys.stderr)

if __name__ == '__main__':  main()  

