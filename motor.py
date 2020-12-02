import sys, serial
from serial.tools import list_ports
from time import sleep


class Motor:
  START, STOP, SHIFT = 0xAA, 0xAB, 0xAC
  ioRates = [1200, 2400, 4800, 9600, 19200, 38400, 57600]
  Ilimits = [0.0, 0.2, 0.3, 0.5, 0.6, 1.0, 2.0, 3.5]
  ioPorts = [port for n, (port, desc, hwid) in enumerate(list_ports.comports(), 1)]
  def __init__(self, ADDR=1, BaudRate=19200, ioPORT='/dev/ttyUSB0', DEBUG=True):
    if not len(self.ioPorts): print('No serial ports found!', file=sys.stderr)
    self.N,     self.ioPort, self.ioRate  = int(ADDR)&0xFF, ioPORT, BaudRate
    self.DEBUG, self.timeout = DEBUG, 0.1
    
  def Status_Byte(self,R):
    self.BS = { 
         "BC"   : (R[1]>>7)&1, 
         "HitK" : (R[1]>>6)&1, 
         "Accu" : (R[1]>>5)&1, 
         "K0"   : (R[1]>>4)&1, 
         "K+"   : (R[1]>>3)&1, 
         "K-"   : (R[1]>>2)&1, 
         "Move" : (R[1]>>1)&1, 
         "Ready":  R[1]&1}
  
  def Set_Logical_Address(self, SN):  # ..................................................Command "0"
    packet = bytes([0x00, 0xAA, ord('W'), ord('S'), SN>>8&0xFF, SN&0xFF, self.ioRates.index(self.ioRate), self.N])
    print(packet)
    ser = serial.Serial(self.ioPort, 600, timeout=5) 
    ser.write(packet)
    ser.close()
    
  # Device will answer to the commands, marked with "*" even if it is busy
    
  def Get_Device_Info(self):   # .........................................................Command 1 *
    self.reply_length=8
    R = self.__Exchange([1])
    return {"Version":str(R[3])+'.'+str(R[4]), "S/N":(R[5]<<8) + R[6]}

  def Repeat_Last_Answer(self):   # ......................................................Command 2 *
    R = self.__Exchange([2])
    
  def Get_Device_Status(self): # .........................................................Command 3 *
    self.reply_length=3
    R = self.__Exchange([3])
    self.Status_Byte(R)

  def Go_With_Acc(self, Steps, StopCond=0): #.............................................Command 4
    N = int(Steps)
    self.__Wait_Until_Ready()
    R = self.__Exchange([4, (N>>24)&0xFF, (N>>16)&0xFF, (N>>8)&0xFF, N&0xFF, 0])
    self.Status_Byte(R)

  def Go_No_Acc(self, Steps, StopCond=0): # ..............................................Command 5
    N = int(Steps)
    self.__Wait_Until_Ready()
    R = self.__Exchange([5, (N>>24)&0xFF, (N>>16)&0xFF, (N>>8)&0xFF, N&0xFF, 0])
    self.Status_Byte(R)

  def Set_Device_Config(self, MoveI, StopI, StopT, CFG): # ...............................Command 6
    MoveI,StopI,StopT,CFG = int(MoveI)&0xFF, int(StopI)&0xFF, int(StopT)&0xFF, int(CFG)&0xFF
    self.__Wait_Until_Ready()
    R = self.__Exchange([6,MoveI,StopI,StopT,CFG])
    self.Status_Byte(R)
  
  def Set_Device_Speed(self, Vmin, Vmax, Acc): # .........................................Command 7
    self.__Wait_Until_Ready()
    R = self.__Exchange([7,(Vmin>>8)&0xFF,Vmin&0xFF,(Vmax>>8)&0xFF,Vmax&0xFF,(Acc>>8)&0xFF,Acc&0xFF])
    self.Status_Byte(R)
  
  def Immediate_Stop(self): #.............................................................Command 8 *
    self.reply_length=3
    R=self.__Exchange([8])
    self.Status_Byte(R)
  
  def Current_Off(self): #................................................................Command 9
    self.__Wait_Until_Ready()
    R=self.__Exchange([9])
    self.Status_Byte(R)
  
  def Save_Data(self): #..................................................................Command 10
    self.__Wait_Until_Ready()
    R=self.__Exchange([10])
    self.Status_Byte(R)
  
  def Blink_on_Sync(self,N=0,Start=1,Step=1): #...........................................Command 11
    self.__Wait_Until_Ready()
    R=self.__Exchange([11,(N>>8)&0xFF,N&0xFF,(Start>>8)&0xFF,Start&0xFF,(Step>>8)&0xFF,Step&0xFF])
    self.Status_Byte(R)
  
  def Get_Rest_Steps(self): #.............................................................Command 12
    self.__Wait_Until_Ready()
    self.reply_length=6
    R=self.__Exchange([12])
    return {"Rest_Steps": int( R[1]<<24 | R[2]<<16 | R[3]<<8 | R[4] - ((R[1]&0x80)<<25))}
  
  def Get_Device_Config(self): # .........................................................Command 13
    self.__Wait_Until_Ready()
    self.reply_length=6
    R=self.__Exchange([13])
    return {"MoveI":R[1], "StopI":R[2], "StopT":R[3], "CFG":R[4]}
  
  def Get_Device_Speed(self): # ..........................................................Command 14
    self.__Wait_Until_Ready()
    self.reply_length=8
    R=self.__Exchange([14])
    return {"Vmin":R[1]*256+R[2], "Vmax":R[3]*256+R[4], "Acc":R[5]*256+R[6]}

  def Frequency_Test(self): #.............................................................Command 15
    self.__Wait_Until_Ready()
    self.reply_length=0
    R=self.__Exchange([15])

  def Set_Period(self,T): #...............................................................Command 16
    self.__Wait_Until_Ready()
    R=self.__Exchange([16,(T>>24)&0xFF, (T>>16)&0xFF, (T>>8)&0xFF, T&0xFF])
    self.Status_Byte(R)

  def Go_Accuartely(self,Steps,Time): # ..................................................Command 17
    S,T=int(Steps),int(Time)
    self.__Wait_Until_Ready()
    R=self.__Exchange([17, (S>>24)&0xFF, (S>>16)&0xFF, (S>>8)&0xFF, S&0xFF, (T>>24)&0xFF, (T>>16)&0xFF, (T>>8)&0xFF, T&0xFF])
    self.Status_Byte(R)

  def Give_Pulse(self): #.................................................................Command 18
    self.__Wait_Until_Ready()
    R=self.__Exchange([18])
    self.Status_Byte(R)

  def Set_Abs_Position(self,K): #.........................................................Command 19
    K=int(K)
    self.__Wait_Until_Ready()
    R=self.__Exchange([19, (K>>24)&0xFF, (K>>16)&0xFF, (K>>8)&0xFF, K&0xFF])
    self.Status_Byte(R)

  def Get_Abs_Position(self): #...........................................................Command 20
    self.__Wait_Until_Ready()
    self.reply_length=6
    R=self.__Exchange([20])
#    return {"Position": int( R[1]<<24 | R[2]<<16 | R[3]<<8 | R[4] - ((R[1]&0x80)<<25)) }
    self.Position=int( R[1]<<24 | R[2]<<16 | R[3]<<8 | R[4] - ((R[1]&0x80)<<25))

  def Block(self): #......................................................................Command 21
    self.__Wait_Until_Ready()
    R=self.__Exchange([21,3]) # Block movement, enable broadcast
    self.Status_Byte(R)
    
  def Release(self): #....................................................................Command 21
    Tmp = self.N
    self.__Wait_Until_Ready() # No answer if N=0 !!!
    self.N=0
    self.__Exchange(bytes[21,4]) # UnBlock movement, disable broadcast
    self.N = Tmp
    
  def Write_User_Data(self,data): #.......................................................Command 22
    S=str(data)
    for i in range(16):
      D=list(S[i*8:(i+1)*8])
      if len(D)>0:
        while len(D)<8: D.extend(' ')
        print (D)
        P=[22,i,ord(D[0]),ord(D[1]),ord(D[2]),ord(D[3]),ord(D[4]),ord(D[5]),ord(D[6]),ord(D[7])]
        self.__Wait_Until_Ready()
        R=self.__Exchange(P)
        self.Status_Byte(R)
      else:
        break
    
  def Read_User_Data(self): #.............................................................Command 23
    S=b''
    for i in range(16):
      self.__Wait_Until_Ready()
      self.reply_length=10
      R=self.__Exchange([23,i])
      for j in range(1,9):
        S+=bytes([R[j]])
    return S

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  def __Wait_Until_Ready(self):
    READY=False
    while not READY:
      self.Get_Device_Status()
      if 'Ready' in self.BS:
        READY=self.BS['Ready']

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

  def __Exchange(self,BODY): # ..................................The Main Packets Exchange Algorythm
# 1. Preparation of outgouing packet:
    OUT, XOR = bytes([self.START, self.N]), self.N
    for byte in BODY:
      XOR ^= byte
      if byte in [self.START, self.STOP, self.SHIFT]:
        OUT += bytes([self.SHIFT + byte - self.START])
      else:
        OUT += bytes([byte])
    if XOR in [self.START, self.STOP, self.SHIFT]:
      OUT += bytes([self.SHIFT + XOR - self.START])
    else:
      OUT += bytes([XOR])
    OUT += bytes([self.STOP]) 
# 2. Exchange:
#    print(OUT)
#    if self.DEBUG: self.Show_String("OUT", OUt)
#    self.lock()
    try: 
      ser = serial.Serial(self.ioPort, self.ioRate, timeout=self.timeout)
    except serial.serialutil.SerialException:
      print('Serial Exception', file=sys.stderr)
      return [0 for elem in range(self.reply_length)]
    ser.flushInput()
    ser.flushOutput()
    ser.write(OUT)
    PIN = ser.read(12)
#    print(PIN)
    ser.close()
#    self.unlock()
#    if self.DEBUG: self.Show_String("REPLY", PIN)
# 3. Translating the Reply:
    REPLY = []
    if len(PIN)>1:
      shift_in_reply, XOR = 0, 0
#      PIN = PIN[0:len(PIN)-1]
      for c in PIN[0:-1]:
        if c==self.SHIFT:
          shift_in_reply = self.START
        else:
          c += shift_in_reply
          REPLY.append(c)
          XOR ^= c
          shift_in_reply=0
# 4. Check possible errors, if any:
      if XOR: 
        print ('Wrong Checksum!');     self.Repeat_Last_Answer()
      if REPLY[0]!=self.N: 
        print ('Not my packet!');      self.Repeat_Last_Answer()
      if len(REPLY)!=self.reply_length: 
        print ('Wrong Packet Length'); self.Repeat_Last_Answer()
      return REPLY
    else:
      return [0 for elem in range(self.reply_length)]

  def Show_String(self,title,s):
    print(title, ' : ')
    for c in s:
      print("Hex:%2X" % (ord(c)))


