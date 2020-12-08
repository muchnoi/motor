import sys, serial
from serial.tools import list_ports
from time import sleep


class Motor:
  START, STOP, SHIFT = 0xAA, 0xAB, 0xAC
  ioPorts = [port for n, (port, desc, hwid) in enumerate(list_ports.comports(), 1)]
  ioRates = [1200, 2400, 4800, 9600, 19200, 38400, 57600]    # Baud Rates supported by controller
  Ilimits = [0.0, 0.2, 0.3, 0.5, 0.6, 1.0, 2.0, 3.5]         # Motor currents limits supported by controller
  rxSizes = [0, 8, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 6, 6, 8, 0, 3, 3, 3, 3, 6, 0, 3, 10] # index is command, value = (number of bytes in reply - 1)
  rxSByte = [3, 4, 5, 6, 7, 8, 9, 10, 11, 16, 17, 18, 19, 22] # list of commands for which device replies with the status byte
  def __init__(self, ADDR=1, BaudRate=38400, ioPORT='/dev/ttyUSB0', DEBUG=False):
    if not len(self.ioPorts): print('No serial ports found!', file=sys.stderr)
    self.N,     self.ioPort, self.ioRate  = int(ADDR)&0xFF, ioPORT, BaudRate
    self.DEBUG, self.timeout = DEBUG, 0.1
    self.BS = {"BC":0, "HitK":0, "Accu":0, "K0":0, "K+":0, "K-":0, "Move":0, "Ready":0} # status byte definition
      
  def Set_Logical_Address(self, SN):  # ..................................................Command "0"
    packet = bytes([0x00, 0xAA, ord('W'), ord('S'), SN>>8&0xFF, SN&0xFF, self.ioRates.index(self.ioRate), self.N])
    if self.DEBUG:
      print('CONFIGURE: ',                            file=sys.stderr, end='')
      for b in packet:     print('|{:02X}'.format(b), file=sys.stderr, end='')
      print('|',                                      file=sys.stderr        )
    ser = serial.Serial(self.ioPort, 600, timeout=5); ser.write(packet); ser.close()
    sleep(1.0)
    
  # Device will answer to the commands, marked with "*" even if it is busy
  def Get_Device_Info(self):   # .........................................................Command 1 *
    R = self.__Exchange([1])
    return {"Version":str(R[3])+'.'+str(R[4]), "S/N":(R[5]<<8) + R[6]}

  def Repeat_Last_Answer(self, cmd, rxSize):   # .........................................Command 2 *
    self.__Exchange([2], cmd = cmd, rxSize = rxSize)
    
  def Get_Device_Status(self): # .........................................................Command 3 *
    self.__Exchange([3])

  def Go_With_Acc(self, Steps, StopCond=0): #.............................................Command 4
    N = int(Steps)
    self.__Exchange([4, (N>>24)&0xFF, (N>>16)&0xFF, (N>>8)&0xFF, N&0xFF, 0])

  def Go_No_Acc(self, Steps, StopCond=0): # ..............................................Command 5
    N = int(Steps)
    self.__Exchange([5, (N>>24)&0xFF, (N>>16)&0xFF, (N>>8)&0xFF, N&0xFF, 0])

  def Set_Device_Config(self, MoveI, StopI, StopT, CFG): # ...............................Command 6
    MoveI,StopI,StopT,CFG = int(MoveI)&0xFF, int(StopI)&0xFF, int(StopT)&0xFF, int(CFG)&0xFF
    self.__Exchange([6,MoveI,StopI,StopT,CFG])
  
  def Set_Device_Speed(self, Vmin, Vmax, Acc): # .........................................Command 7
    self.__Exchange([7,(Vmin>>8)&0xFF,Vmin&0xFF,(Vmax>>8)&0xFF,Vmax&0xFF,(Acc>>8)&0xFF,Acc&0xFF])
  
  def Immediate_Stop(self): #.............................................................Command 8 *
    self.__Exchange([8])
  
  def Current_Off(self): #................................................................Command 9
    self.__Exchange([9])
  
  def Save_Data(self): #..................................................................Command 10
    self.__Exchange([10])
  
  def Blink_on_Sync(self,N=0,Start=1,Step=1): #...........................................Command 11
    self.__Exchange([11,(N>>8)&0xFF,N&0xFF,(Start>>8)&0xFF,Start&0xFF,(Step>>8)&0xFF,Step&0xFF])
  
  def Get_Rest_Steps(self): #.............................................................Command 12
    R = self.__Exchange([12])
    return {"Rest_Steps": int( R[1]<<24 | R[2]<<16 | R[3]<<8 | R[4] - ((R[1]&0x80)<<25))}
  
  def Get_Device_Config(self): # .........................................................Command 13
    R = self.__Exchange([13])
    return {"MoveI":R[1], "StopI":R[2], "StopT":R[3], "CFG":R[4]}
  
  def Get_Device_Speed(self): # ..........................................................Command 14
    R = self.__Exchange([14])
    return {"Vmin":R[1]*256+R[2], "Vmax":R[3]*256+R[4], "Acc":R[5]*256+R[6]}

  def Frequency_Test(self): #.............................................................Command 15
    self.__Exchange([15])

  def Set_Period(self,T): #...............................................................Command 16
    self.__Exchange([16,(T>>24)&0xFF, (T>>16)&0xFF, (T>>8)&0xFF, T&0xFF])

  def Go_Accuartely(self, Steps, Time): # ................................................Command 17
    S, T = int(Steps), int(Time)
    self.__Exchange([17, (S>>24)&0xFF, (S>>16)&0xFF, (S>>8)&0xFF, S&0xFF, (T>>24)&0xFF, (T>>16)&0xFF, (T>>8)&0xFF, T&0xFF])

  def Give_Pulse(self): #.................................................................Command 18
    self.__Exchange([18])

  def Set_Abs_Position(self,K): #.........................................................Command 19
    K = int(K)
    self.__Exchange([19, (K>>24)&0xFF, (K>>16)&0xFF, (K>>8)&0xFF, K&0xFF])

  def Get_Abs_Position(self): #...........................................................Command 20
    R = self.__Exchange([20])
    self.Position = int( R[1]<<24 | R[2]<<16 | R[3]<<8 | R[4] - ((R[1]&0x80)<<25))

  def Block(self): #......................................................................Command 21
    self.__Exchange([21,3]) # Block movement, enable broadcast
    
  def Release(self): #....................................................................Command 21
    Tmp = self.N
#   No answer if N=0 !!!
    self.N=0
    self.__Exchange(bytes[21,4]) # UnBlock movement, disable broadcast
    self.N = Tmp
    
  def Write_User_Data(self,data): #.......................................................Command 22
    S = str(data)
    for i in range(16):
      D = list(S[i*8:(i+1)*8])
      if len(D) > 0:
        while len(D) < 8: D.extend(' ')
        print (D)
        P = [22, i, ord(D[0]), ord(D[1]), ord(D[2]), ord(D[3]), ord(D[4]), ord(D[5]), ord(D[6]), ord(D[7])]
        self.__Exchange(P)
      else:
        break
    
  def Read_User_Data(self): #.............................................................Command 23
    S = b''
    for i in range(16):
      R = self.__Exchange([23,i])
      for j in range(1,9): S += bytes([R[j]])
    return S

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  def __Exchange(self, BODY, cmd = 0, rxSize = 0): # ............The Main Packets Exchange Procedure
#   1. Preparation of outgouing packet:
    Tx, XOR = bytes([self.START, self.N]), self.N
    if not cmd: # i.e. in "normal" case
      cmd    = BODY[0]           # command number
      rxSize = self.rxSizes[cmd] # expected length of reply
    for byte in BODY:
      XOR ^= byte
      if byte in [self.START, self.STOP, self.SHIFT]:
        Tx += bytes([self.SHIFT + byte - self.START])
      else:
        Tx += bytes([byte])
    if XOR in [self.START, self.STOP, self.SHIFT]:
      Tx += bytes([self.SHIFT + XOR - self.START])
    else:
      Tx += bytes([XOR])
    Tx += bytes([self.STOP]) 
#   2. Exchange:
    if self.DEBUG: self.Show_String("->", Tx)
    try: 
      ser = serial.Serial(self.ioPort, self.ioRate, timeout=self.timeout)
    except serial.serialutil.SerialException:
      print('Serial Exception', file=sys.stderr)
      return [0 for elem in range(rxSize)]
#    ser.flushInput()
#    ser.flushOutput()
    ser.write(Tx)
    Rx = ser.read(25)
    ser.close()
    if self.DEBUG: self.Show_String("<-", Rx)
#   3. Translating the Reply:
    REPLY = []
    if bool(Rx):
      shift_in_reply, XOR = 0, 0
      for c in Rx[0:-1]:
        if c==self.SHIFT:
          shift_in_reply = self.START
        else:
          c += shift_in_reply
          REPLY.append(c)
          XOR ^= c
          shift_in_reply = 0
#   4. Check possible errors, if any:
      success = False
      if XOR:                    print ('Wrong Checksum!',     file = sys.stderr)
      elif REPLY[0]   != self.N: print ('Not my packet!',      file = sys.stderr)
      elif len(REPLY) != rxSize: print ('Wrong Packet Length', file = sys.stderr)
      else:                      success = True
      if success:
        if cmd in self.rxSByte:
          R = REPLY[1]
          self.BS["BC"]    = (R>>7)&1
          self.BS["HitK"]  = (R>>6)&1
          self.BS["Accu"]  = (R>>5)&1
          self.BS["K0"]    = (R>>4)&1
          self.BS["K+"]    = (R>>3)&1
          self.BS["K-"]    = (R>>2)&1
          self.BS["Move"]  = (R>>1)&1
          self.BS["Ready"] =  R    &1
          return
        else:
          return REPLY
      else: self.Repeat_Last_Answer(cmd, rxSize)
    else:
      return [0 for elem in range(rxSize)]

  def Show_String(self,title,s):
    print(title, file = sys.stderr, end='')
    if '>' in title: 
      L = 12
      for b in s: 
        L -= 1 
        print('|{:02X}'.format(b), file=sys.stderr, end='')
      print('|' + '   '*L, file = sys.stderr, end = '')  
    else:              
      for b in s: 
        print('|{:02X}'.format(b), file=sys.stderr, end='')
      if s: print('|',    file = sys.stderr)
      else: print('None', file = sys.stderr)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  def lock(self):
    while True:
      with open('_lock_','r+b') as f: 
#        raw_input('pause 1')
        B = f.readline()
        if not 'busy' in B:
          f.seek(0)
          f.write(b'busy\n')
          f.truncate(5)
          break
      sleep(0.1)
#    raw_input('pause 2')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  def unlock(self):
    with open('_lock_','w+b') as f: f.write(b'free\n')
#    raw_input('pause 3')

