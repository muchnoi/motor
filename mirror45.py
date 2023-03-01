#!/usr/bin/env python3
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon
import sys, axis45
from motor import Motor

class Application(QtWidgets.QMainWindow, axis45.Ui_MainWindow):
  css = { 'idle': 'QPushButton{color: white;} QPushButton:hover{color:    yellow;} QPushButton:pressed{color: darkgreen;}',
          'move': 'QPushButton{color: green;} QPushButton:hover{color: darkgreen;} QPushButton:pressed{color: darkgreen;}',
          'wait': 'QPushButton{color:  gray;} QPushButton:hover{color:      gray;} QPushButton:pressed{color:      gray;}',
          'stop': 'QPushButton{color:   red;} QPushButton:hover{color:   darkred;} QPushButton:pressed{color:       red;}'}
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle('Mirror Control')
    self.setWindowIcon(QIcon('wheels.png'))
    self.M = []
    self.M.append(Motor(ADDR=1, BaudRate=19200, ioPORT='/dev/Motors', DEBUG=False))
    self.M.append(Motor(ADDR=2, BaudRate=19200, ioPORT='/dev/Motors', DEBUG=False))
#   Мотор и количество шагов для поворота измерителя мощности на 90 градусов:
    self.PowMet = Motor(ADDR=5, BaudRate=19200, ioPORT='/dev/Motors', DEBUG=False)
    self.Turn   = 200
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
    self.t = [QTimer(), QTimer()]
    self.t[0].setSingleShot(True);             self.t[1].setSingleShot(True)
    self.t[0].setInterval(200);                self.t[1].setInterval(2000)
    self.t[0].timeout.connect(self.Status);    self.t[1].timeout.connect(self.LaserAuto)
    for name, content in self.arrows.items():  content[0].clicked.connect(self.Go)
    self.PowMet.Get_Abs_Position()
    if self.PowMet.Position==-self.Turn: self.LaserON.setChecked(True)
    elif self.PowMet.Position==0:        self.LaserOFF.setChecked(True)
    self.LaserON.toggled.connect( self.LaserControl)
    self.AutoMode.toggled.connect(self.LaserAuto); self.howlong = 0
    self.ResetButt.clicked.connect( self.thisisZero)
    self.ReturnButt.clicked.connect(self.returntoZero)
#    self.Status()

  def LaserControl(self):
    self.PowMet.Get_Abs_Position()
    if self.LaserON.isChecked():
      if self.PowMet.Position==0: self.PowMet.Go_With_Acc(-self.Turn)
      for v in self.arrows.values():
        v[0].setStyleSheet(self.css['idle']); v[0].setEnabled(True)
    else:
      if self.PowMet.Position==-self.Turn: self.PowMet.Go_With_Acc(self.Turn)
      for v in self.arrows.values():
        v[0].setStyleSheet(self.css['wait']); v[0].setEnabled(False)
        self.t[0].stop()

  def LaserAuto(self):
    if self.AutoMode.isChecked():            # если мы в автоматическом режиме
      if not self.howlong:                   # если только что в него попали
        self.LaserON.setEnabled(False)       # отключаем ручное управление
        self.LaserOFF.setEnabled(False)      # отключаем ручное управление
        self.howlong = 1                     # начинаем считать
      if self.LaserON.isChecked():           # если лазер включен
        if not self.Ie():                    # а тока нет
          self.howlong += 1                  # думаем (продолжаем считать)
          if self.howlong > 10.:             # если нет уже давно
            self.howlong =  0                # сбрасываем счетчик
            self.LaserOFF.setChecked(True)   # выключаем лазер
      elif self.LaserOFF.isChecked():        # если же лазер выключен
        if self.Ie():                        # а ток есть
          self.howlong += 1                  # думаем
          if self.howlong > 10.:             # если есть уже давно
            self.howlong =  0                # сбрасываем счетчик
            self.LaserON.setChecked(True)    # включаем лазер
      print(self.howlong)
      self.t[1].start()                      # запускаем таймер для продолжения наблюдений
    else:                                    # если мы в ручном режиме
      self.t[1].stop()                       # останавливаем таймер
      self.LaserON.setEnabled(True)          # включаем ручное управление
      self.LaserOFF.setEnabled(True)         # включаем ручное управление
      print ('Manual')

  def Ie(self):
    return False

  def Go(self):
    name = self.sender().objectName()
    butt, signs   = self.arrows[name][0], self.arrows[name][1:3]
    for i in [0,1]:
      if signs[i]:
        j = (1+signs[i])//2
        self.buttons[i][j].setStyleSheet(  self.css['move'])
        self.M[i].Go_With_Acc(signs[i] * self.StepsBox.value())
    self.t[0].start()

  def returntoZero(self):
    for i in [0,1]:
      if self.M[i].Position:
        self.buttons[i][self.M[i].Position<0].setStyleSheet(self.css['move'])
        self.M[i].Go_With_Acc(-self.M[i].Position)
    self.t[0].start()

  def thisisZero(self):
    for i in [0,1]: self.M[i].Set_Abs_Position(0)
    self.t[0].start()

  def Status(self):
    idle = True
    for i in [0,1]:
      self.M[i].Get_Device_Status()
      ready, trailers = self.M[i].BS['Ready'], [self.M[i].BS['K-'], self.M[i].BS['K+']]
      if ready:
        for j in [0,1]:
          if trailers[j]: self.buttons[i][j].setStyleSheet(self.css['stop'])
          else:           self.buttons[i][j].setStyleSheet(self.css['idle'])
        self.M[i].Get_Abs_Position()
      idle = idle and ready
    if not idle:
      self.t[0].start()
    else:
#     print(self.M[0].Position,  self.M[1].Position)
      self.YlcdNumber.display((- self.M[0].Position + self.M[1].Position)//2)
      self.XlcdNumber.display((- self.M[0].Position - self.M[1].Position)//2)

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
