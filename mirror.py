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
    self.setWindowIcon(QIcon('wheels.png'))
    self.M = []
    self.M.append(Motor(ADDR=1, BaudRate=38400, ioPORT='/dev/ttyUSB0', DEBUG=False))
    self.M.append(Motor(ADDR=2, BaudRate=38400, ioPORT='/dev/ttyUSB0', DEBUG=False))
    self.counters = [self.YlcdNumber, self.XlcdNumber]
    self.arrows   = {'UpButton'   :   [self.UpButton, 0, +1], 'DownButton' : [self.DownButton, 0, -1],
                     'RightButton':[self.RightButton, 1, +1], 'LeftButton' : [self.LeftButton, 1, -1]}
    self.buttons  = [[self.UpButton, self.DownButton], [self.RightButton, self.LeftButton]]
    self.initWidgets()

  def closeEvent(self, event):
    event.accept()

  def initWidgets(self):
    self.timer = QTimer()
    self.timer.setSingleShot(True)
    self.timer.setInterval(200)
    self.ManualButton.setChecked(True)
    self.timer.timeout.connect(       self.Status)
    self.UpButton.clicked.connect(    self.Go)
    self.RightButton.clicked.connect( self.Go)
    self.DownButton.clicked.connect(  self.Go)
    self.LeftButton.clicked.connect(  self.Go)
    self.ResetButton.clicked.connect( self.thisisZero)
    self.ReturnButton.clicked.connect(self.returntoZero)
    self.Status()
      
  def Go(self):
    sender = self.sender()
    butt, yorx, sign   = self.arrows[sender.objectName()] 
    butt.setStyleSheet(self.css['move'])
    self.M[yorx].Go_With_Acc(sign * self.StepsBox.value())
    self.Status()
    
  def thisisZero(self):
    for i in [0,1]:
      self.M[i].Set_Abs_Position(0)
      self.counters[i].display(0)
    self.Status()
  
  def returntoZero(self):
    for i in [0,1]:
      self.M[i].Get_Abs_Position()
      self.buttons[i][self.M[i].Position>0].setStyleSheet(self.css['move'])
      self.M[i].Go_With_Acc(-self.M[i].Position)
    self.Status()

  def Status(self):
    idle = True
    for i in [0,1]:
      self.M[i].Get_Device_Status()
      ready, trailers = self.M[i].BS['Ready'], [self.M[i].BS['K+'], self.M[i].BS['K-']]
      if ready:
        for j in [0,1]:
          if trailers[j]: self.buttons[i][j].setStyleSheet(self.css['stop'])
          else:           self.buttons[i][j].setStyleSheet(self.css['idle'])
        self.M[i].Get_Abs_Position()
        self.counters[i].display(self.M[i].Position)
      idle = idle and ready
    if not idle: self.timer.start()

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

