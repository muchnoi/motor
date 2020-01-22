import serial
from time import sleep

class Motor:
  
  def __init__(self, ADDR=1, BaudRate=19200, ioPORT='/dev/ttyUSB0', DEBUG=False):
    self.N,     self.ioPORT  = int(ADDR)&0xFF, ioPORT
    self.DEBUG, self.timeout = DEBUG, 0.1
    self.ioRATE = { 1200:0, 2400:1, 4800:2, 9600:3, 19200:4, 38400:5, 57600:6 }
    self.BR = BaudRate
    self.START, self.STOP, self.SHIFT = chr(0xAA), chr(0xAB), chr(0xAC)

  def Configuration_Byte(self,CFG):
    B0 = 0 if ('4'    in CFG['Mode']) else 1
    B2 = 0 if ('Closed' in CFG['K-']) else 1
    B3 = 0 if ('Closed' in CFG['K+']) else 1
    B4 = 0 if ('Closed' in CFG['K0']) else 1
    B5 = int(CFG['Soft_Trailers'])
    B6 = int(CFG['Leave_Trailer'])
    B7 = int(CFG['Accl_On_Leave'])
    return B0 + B2*4 + B3*8 + B4*16 + B5*32 + B6*64 + B7*128
    
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
  
  def Set_Logical_Address(self,SN):  # ...................................................Command "0"
#    packet = '\x00\xAAWS' + chr(SN&0xFF00) + chr(SN&0xFF) + chr(self.ioRATE[self.BR]) + chr(self.N) 
    packet = '\x00\xAAWS' + chr((SN>>8)&0xFF) + chr(SN&0xFF) + chr(self.ioRATE[self.BR]) + chr(self.N) 
    ser = serial.Serial(self.ioPORT, 600, timeout=5) 
    ser.write(packet)
    ser.close()
    
  # Device will answer to the commands, marked with "*" even if it is busy
    
  def Get_Device_Info(self):   # .........................................................Command 1 *
    self.reply_length=8
    R=self.__Exchange([1])
    return {"Version":str(R[3])+'.'+str(R[4]), "S/N":(R[5]<<8) + R[6]}

  def Repeat_Last_Answer(self):   # ......................................................Command 2 *
    R=self.__Exchange([2])
    
  def Get_Device_Status(self): # .........................................................Command 3 *
    self.reply_length=3
    R=self.__Exchange([3])
    self.Status_Byte(R)

  def Go_With_Acc(self,Steps,StopCond=0): # ..............................................Command 4
    N=int(Steps)
    self.__Wait_Until_Ready()
    R=self.__Exchange([4, (N>>24)&0xFF, (N>>16)&0xFF, (N>>8)&0xFF, N&0xFF, 0])
    self.Status_Byte(R)

  def Go_No_Acc(self,Steps,StopCond=0): # ................................................Command 5
    N=int(Steps)
    self.__Wait_Until_Ready()
    R=self.__Exchange([5, (N>>24)&0xFF, (N>>16)&0xFF, (N>>8)&0xFF, N&0xFF, 0])
    self.Status_Byte(R)

  def Set_Device_Config(self,MoveI,StopI,StopT,CFG): # ...................................Command 6
    MoveI,StopI,StopT,CFG = int(MoveI)&0xFF, int(StopI)&0xFF, int(StopT)&0xFF, int(CFG)&0xFF
    self.__Wait_Until_Ready()
    R=self.__Exchange([6,MoveI,StopI,StopT,CFG])
    self.Status_Byte(R)
  
  def Set_Device_Speed(self,Vmin,Vmax,Acc): # ............................................Command 7
    self.__Wait_Until_Ready()
    R=self.__Exchange([7,(Vmin>>8)&0xFF,Vmin&0xFF,(Vmax>>8)&0xFF,Vmax&0xFF,(Acc>>8)&0xFF,Acc&0xFF])
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
    self.__Exchange([21,4]) # UnBlock movement, disable broadcast
    self.N = Tmp
    
  def Write_User_Data(self,data): #.......................................................Command 22
    S=str(data)
    for i in range(16):
      D=list(S[i*8:(i+1)*8])
      if len(D)>0:
        while len(D)<8: D.extend(' ')
        print D
        P=[22,i,ord(D[0]),ord(D[1]),ord(D[2]),ord(D[3]),ord(D[4]),ord(D[5]),ord(D[6]),ord(D[7])]
        self.__Wait_Until_Ready()
        R=self.__Exchange(P)
        self.Status_Byte(R)
      else:
        break
    
  def Read_User_Data(self): #.............................................................Command 23
    S=''
    for i in range(16):
      self.__Wait_Until_Ready()
      self.reply_length=10
      R=self.__Exchange([23,i])
      for j in range(1,9):
        S+=chr(R[j])
    return S

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  def __Wait_Until_Ready(self):
    READY=False
    while not READY:
      self.Get_Device_Status()
      if self.BS.has_key('Ready'):
        READY=self.BS['Ready']

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  def lock(self):
    while True:
      with open('_lock_','r+b') as f: 
#        raw_input('pause 1')
        B = f.readline()
        if not 'busy' in B:
          f.seek(0)
          f.write('busy\n')
          f.truncate(5)
          break
      sleep(0.1)
#    raw_input('pause 2')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  def unlock(self):
    with open('_lock_','w+b') as f: f.write('free\n')
#    raw_input('pause 3')

  def __Exchange(self,BODY): # ..................................The Main Packets Exchange Algorythm
# 1. Preparation of outgouing packet:
    OUT, XOR = self.START + chr(self.N), self.N
    for byte in BODY:
      XOR ^= byte
      if chr(byte) in [self.START, self.STOP, self.SHIFT]:
        OUT += self.SHIFT + chr(byte - ord(self.START))
      else:
        OUT += chr(byte)
    if chr(XOR) in [self.START, self.STOP, self.SHIFT]:
      OUT += self.SHIFT + chr(XOR - ord(self.START))
    else:
      OUT += chr(XOR)
    OUT += self.STOP 
# 2. Exchange:
    if self.DEBUG: self.Show_String("OUT",OUT)
    self.lock()
    try: 
      ser = serial.Serial(self.ioPORT, self.BR, timeout=self.timeout)
    except serial.serialutil.SerialException:
      return [0 for elem in range(self.reply_length)]
    ser.flushInput()
    ser.flushOutput()
    ser.write(OUT)
    PIN = ser.read(12)
    ser.close()
    self.unlock()
    if self.DEBUG: self.Show_String("REPLY",PIN)
# 3. Translating the Reply:
    REPLY = []
    if len(PIN)>1:
      shift_in_reply, XOR = 0, 0
      PIN=PIN[0:len(PIN)-1]
      for c in PIN:
        if c==self.SHIFT:
          shift_in_reply=ord(self.START)
        else:
          REPLY.append(ord(c)+shift_in_reply)
          XOR^=ord(c)+shift_in_reply
          shift_in_reply=0
# 4. Check possible errors, if any:
      if XOR: 
        print 'Wrong Checksum!';     self.Repeat_Last_Answer()
      if REPLY[0]!=self.N: 
        print 'Not my packet!';      self.Repeat_Last_Answer()
      if len(REPLY)!=self.reply_length: 
        print 'Wrong Packet Length'; self.Repeat_Last_Answer()
      return REPLY
    else:
      return [0 for elem in range(self.reply_length)]

  def Show_String(self,title,s):
    print title + ":"
    for c in s:
      print "Dec: %03d | Hex:%2X | Str:%1c" % (ord(c), ord(c), c)


