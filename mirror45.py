#!/usr/bin/env python3
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon
import sys, axis45
from motor import Motor
from time import sleep

class Application(QtWidgets.QMainWindow, axis45.Ui_MainWindow):
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
    self.M.append(Motor(ADDR=1, BaudRate=38400, ioPORT='/dev/ttyUSB0', DEBUG=False))
    self.counters = [self.YlcdNumber, self.XlcdNumber]
#   M[0] стоит слева внизу если смотреть на зеркало со стороны моторов, 
#   если он толкает зеркало (signs = [+1, 0]), луч идет влево и вниз
#   если он тянет зеркало   (signs = [-1, 0]), луч идет вправо и вверх
#   M[1] стоит справа внизу если смотреть на зеркало со стороны моторов,
#   если он толкает зеркало (signs = [0, +1]), луч идет влево и вверх
#   если он тянет зеркало   (signs = [0, -1]), луч идет вправо и вниз
#   тогда вверх = [-1, +1] вниз = [+1, -1] вправо = [-1, -1] влево = [+1, +1]
#                     object name      object        signs:  M[0], M[1] 
    self.arrows   = {'DownButt'     : [self.DownButt,        +1,   -1],
                     'LeftButt'     : [self.LeftButt,        +1,   +1], 
                     'LeftDownButt' : [self.LeftDownButt,    +1,    0], 
                     'LeftUpButt'   : [self.LeftUpButt,       0,   +1], 
                     'RightButt'    : [self.RightButt,       -1,   -1],
                     'RightDownButt': [self.RightDownButt,    0,   -1], 
                     'RightUpButt'  : [self.RightUpButt,     -1,    0], 
                     'UpButt'       : [self.UpButt,          -1,   +1]}
    self.buttons  = [[self.RightUpButt, self.LeftDownButt], [self.RightDownButt, self.LeftUpButt]]
    self.initWidgets()

  def closeEvent(self, event):
    event.accept()
    
  def initWidgets(self):
    self.timer = QTimer()
    self.timer.setSingleShot(True)
    self.timer.setInterval(200)
    self.ManualButton.setChecked(True)
    self.timer.timeout.connect(       self.Status)
    for name, content in self.arrows.items(): 
       content[0].clicked.connect(self.Go)
    self.ResetButt.clicked.connect( self.thisisZero)
    self.ReturnButt.clicked.connect(self.returntoZero)
    self.Status()
      
  def Go(self):
    name = self.sender().objectName()
    butt, signs   = self.arrows[name][0], self.arrows[name][1:3]
    for i in [0,1]:
      if signs[i]:
        j = (1+signs[i])//2
        self.buttons[i][j].setStyleSheet(  self.css['move'])
        self.M[i].Go_With_Acc(signs[i] * self.StepsBox.value())
        sleep(1) # !!!!!!
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
      sleep(1) # !!!!!!
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
      idle = idle and ready
    if not idle: 
      self.timer.start()
    else:
      print(self.M[0].Position, self.M[1].Position)
      Y = self.M[1].Position - self.M[0].Position
      X = self.M[0].Position - self.M[1].Position
      self.counters[0].display(Y)
      self.counters[1].display(X)

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

