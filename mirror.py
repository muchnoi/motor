#!/usr/bin/env python3
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
import sys, doubleaxis
from motor import Motor

class Application(QtWidgets.QMainWindow, doubleaxis.Ui_MainWindow):
  css = { 'idle': 'QPushButton{color: white;} QPushButton:hover{color:    yellow;} QPushButton:pressed{color: darkgreen;}',
          'move': 'QPushButton{color: green;} QPushButton:hover{color: darkgreen;} QPushButton:pressed{color: darkgreen;}',
          'stop': 'QPushButton{color:   red;} QPushButton:hover{color:   darkred;} QPushButton:pressed{color: red;}'}
  def __init__(self): 
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle('Mirror Control')
    self.setWindowIcon(QIcon('desk.png'))
    self.M = [Motor(ADDR=1,BaudRate=38400,ioPORT='/dev/ttyUSB0',DEBUG=False), Motor(ADDR=1,BaudRate=38400,ioPORT='/dev/ttyUSB0',DEBUG=False)]
    self.counters = [self.YlcdNumber, self.XlcdNumber]
    self.arrows = {'UpButton'   :   [self.UpButton, 0, +1], 
                   'RightButton':[self.RightButton, 1, +1],
                   'DownButton' : [self.DownButton, 0, -1],
                   'LeftButton' : [self.LeftButton, 1, -1]}
    self.initWidgets()
    self.initMotors()

  def closeEvent(self, event):
    event.accept()

  def initWidgets(self):
    self.timer = QTimer()
    self.timer.setSingleShot(True)
    self.timer.setInterval(200)
    self.ManualButton.setChecked(True)
    self.timer.timeout.connect(       self.Wait)
    self.UpButton.clicked.connect(    self.Go)
    self.RightButton.clicked.connect( self.Go)
    self.DownButton.clicked.connect(  self.Go)
    self.LeftButton.clicked.connect(  self.Go)
    self.ResetButton.clicked.connect( self.thisisZero)
    self.ReturnButton.clicked.connect(self.returntoZero)
    
  def initMotors(self):
    for name, conf in self.arrows.items():
      self.butt, self.yorx, self.sign = conf 
      self.butt.setStyleSheet(self.css['move'])
      self.engn = self.M[self.yorx]
      self.Wait()
      
  def thisisZero(self):
    for i in [0,1]:
      self.M[i].Set_Abs_Position(0)
      self.counters[i].display(0)
      self.Wait()
  
  def returntoZero(self):
    for i in [0,1]:
      self.yorx, self.engn = i, self.M[i]
      self.engn.Get_Abs_Position()
      if self.engn.Position<0: self.sign = +1
      else:                    self.sign = -1
      for k,v in self.arrows.items():
        if v[1]==i and v[2]==self.sign:
          self.butt = v[0]
          self.butt.setStyleSheet(self.css['move'])
          self.engn.Go_With_Acc(self.sign*abs(self.engn.Position))
          self.Wait()
          break   

  def Go(self):
    sender = self.sender()
    self.butt, self.yorx, self.sign   = self.arrows[sender.objectName()] 
    self.butt.setStyleSheet(self.css['move'])
    self.engn = self.M[self.yorx]
    self.engn.Go_With_Acc(self.sign * self.StepsBox.value())
    self.Wait()
    
  def Wait(self):
    self.engn.Get_Device_Status()
    if self.engn.BS['Ready']:                
      self.butt.setStyleSheet(self.css['idle'])
      self.engn.Get_Abs_Position()
      if   self.yorx == 0: self.YlcdNumber.display(self.engn.Position)
      elif self.yorx == 1: self.XlcdNumber.display(self.engn.Position)
    else:
      self.timer.start()
    if (self.engn.BS['K+'] and self.sign>0) or (self.engn.BS['K-'] and self.sign<0): 
      self.butt.setStyleSheet(self.css['stop'])

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

