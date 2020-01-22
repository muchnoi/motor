#!/usr/bin/env python

from Tkinter import *
from random import random
from time import sleep
from interaction import Interaction


class Stepper(Frame,Interaction): # class class class class class class class class

  def __init__(self, master=None,name=None):
    Frame.__init__(self, master)
    Interaction.__init__(self)
    self.oops=master
    self.grid()
    self.createWidgets()
    self.name=name
   
  def __del__(self, master=None):
    Frame.__del__(self, master)
    Interaction.__del__(self)

  def Status_Frame(self):
    self.statuskeys=[ 
      {'K+'   :[ {'text':'K+',  'bg':'#00ff00'}, {'text':'K+',   'bg':'#ff0000'} ]},
      {'K-'   :[ {'text':'K-',  'bg':'#00ff00'}, {'text':'K-',   'bg':'#ff0000'} ]},
      {'K0'   :[ {'text':'K0',  'bg':'#00ff00'}, {'text':'K0',   'bg':'#ff0000'} ]},
      {'HitK' :[ {'text':'HitK','bg':'#f0f0f0'}, {'text':'HitK', 'bg':'#ff0000'} ]},
      {'Ready':[ {'text':'Busy','bg':'#ff0000'}, {'text':'Ready','bg':'#00ff00'} ]},
      {'Move' :[ {'text':'Stay','bg':'#00ff00'}, {'text':'Move', 'bg':'#ff0000'} ]},
      {'Accu' :[ {'text':'Accu','bg':'#f0f0f0'}, {'text':'Accu', 'bg':'#00ff00'} ]} ]
    self.status=[]
    self.StatusFrame = Frame(self, borderwidth=2, relief=RIDGE, height=200, width=60)
    self.StatusFrame.columnconfigure(0,minsize=50)
    for k in self.statuskeys:
      v=k.values()
      self.status.append(Label(self.StatusFrame, text=v[0][0]['text'],  borderwidth=2, relief=RIDGE, bg='#f0f0f0'))
      self.status[-1].grid(sticky=E+W,padx=2,pady=3)
    self.StatusFrame.grid_propagate(0)
    
  def Communication_Frame(self):
    self.Dev, self.ioPort, self.BaudRate, self.SN = StringVar(), StringVar(), IntVar(), StringVar()
    self.BaudRate.set(19200); self.ioPort.set('/dev/ttyUSB0')
    self.Dev.set(5)
    self.CommunicationFrame = Frame(self, borderwidth=2, relief=RIDGE, height=70, width=440)
    self.DevLabel=Label(self.CommunicationFrame, text='Device:', anchor=E)
    self.DevEntry=Entry(self.CommunicationFrame, width=3, textvariable=self.Dev, bg='#ffffff')
    self.ioPortLabel=Label(self.CommunicationFrame, text='I/O Port:', anchor=E)
    self.ioPortMenu=OptionMenu(self.CommunicationFrame, self.ioPort, 'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7',
                                                                     '/dev/ttyS0', '/dev/ttyS1', '/dev/ttyS2', '/dev/ttyS3', 
                                                                     '/dev/ttyUSB0')
    self.BRLabel=Label(self.CommunicationFrame, text=' BaudRate:', anchor=E)
    self.BRMenu=OptionMenu(self.CommunicationFrame, self.BaudRate, 1200, 2400, 4800, 9600, 19200, 38400, 57600)
    self.ConnectButton = Button (self.CommunicationFrame, text="Connect", command=self.Connect, anchor=S )
    self.VersionLabel=Label(self.CommunicationFrame, text='No connection', anchor=CENTER)
    self.SNLabel=Label(self.CommunicationFrame, text=' S/N:', anchor=E)
    self.SNEntry=Entry(self.CommunicationFrame, width=3, textvariable=self.SN, bg='#ffffff')
    self.SetButton = Button (self.CommunicationFrame, text="Set", command=self.SetAddr, activeforeground='#ff0000', anchor=S )

    self.CommunicationFrame.columnconfigure(0,minsize=90)
    self.CommunicationFrame.columnconfigure(1,minsize=60)
    self.CommunicationFrame.columnconfigure(2,minsize=80)
    self.CommunicationFrame.columnconfigure(3,minsize=140)
    self.CommunicationFrame.columnconfigure(4,minsize=40)
    self.CommunicationFrame.columnconfigure(5,minsize=40)

    self.DevLabel.grid(      row=0, column=0, sticky=E)
    self.DevEntry.grid(      row=0, column=1, sticky=E+W)
    self.ioPortLabel.grid(   row=0, column=2, sticky=E)
    self.ioPortMenu.grid(    row=0, column=3, sticky=E+W)
    self.SNLabel.grid(       row=0, column=4, sticky=E,padx=2)
    self.SNEntry.grid(       row=0, column=5, sticky=E+W,padx=2)
    self.SetButton.grid(     row=1, column=4, columnspan=2,sticky=E+W,padx=2)
    self.VersionLabel.grid(  row=1, column=0, sticky=E+W)
    self.ConnectButton.grid( row=1, column=1, sticky=E+W)
    self.BRLabel.grid(       row=1, column=2, sticky=E)
    self.BRMenu.grid(        row=1, column=3, sticky=E+W)

    self.CommunicationFrame.grid_propagate(0)
    
  def Configuration_Frame(self):
    self.NPhase = IntVar()
    self.PT,self.NT,self.OT = IntVar(),IntVar(),IntVar()
    self.ST,self.LT,self.AT = IntVar(),IntVar(),IntVar()
    self.IMove, self.IStop, self.TStop = StringVar(), StringVar(), StringVar()

    self.ConfigurationFrame = Frame(self, borderwidth=2, relief=RIDGE, height=200, width=300)
    self.ConfigurationLabel=Label(self.ConfigurationFrame, text='Configuration', bg='#A0A0C0', anchor=CENTER)
    self.IMoveLabel=Label(self.ConfigurationFrame, text='I move:', anchor=E)
    self.IMoveMenu=OptionMenu(self.ConfigurationFrame, self.IMove,'0 A','0.2 A','0.3 A','0.5 A','0.6 A','1.0 A','2.0 A','3.5 A')
    self.IStopLabel=Label(self.ConfigurationFrame, text='I stop:', anchor=E)
    self.IStopMenu=OptionMenu(self.ConfigurationFrame, self.IStop,'0 A','0.2 A','0.3 A','0.5 A','0.6 A','1.0 A','2.0 A','3.5 A')
    self.TStopLabel=Label(self.ConfigurationFrame, text='T stop:', anchor=E)
    self.TStopEntry=Entry(self.ConfigurationFrame, width=3, textvariable=self.TStop, bg='#ffffff')
    self.ApplyITButton = Button (self.ConfigurationFrame, text="Apply", command=self.Set_Configuration, anchor=CENTER )

    self.PhaseLabel=Label(self.ConfigurationFrame, text='Phase:', anchor=E)
    self.Phase4Button=Radiobutton(self.ConfigurationFrame,variable=self.NPhase,value=0,text='4')
    self.Phase8Button=Radiobutton(self.ConfigurationFrame,variable=self.NPhase,value=1,text='8')
    self.PTLabel=Label(self.ConfigurationFrame, text='K+:', anchor=E)
    self.PTNOButton=Radiobutton(self.ConfigurationFrame,variable=self.PT,value=0,text='x')
    self.PTNCButton=Radiobutton(self.ConfigurationFrame,variable=self.PT,value=1,text='o')
    self.NTLabel=Label(self.ConfigurationFrame, text='K-:', anchor=E)
    self.NTNOButton=Radiobutton(self.ConfigurationFrame,variable=self.NT,value=0,text='x')
    self.NTNCButton=Radiobutton(self.ConfigurationFrame,variable=self.NT,value=1,text='o')
    self.OTLabel=Label(self.ConfigurationFrame, text='K0:', anchor=E)
    self.OTNOButton=Radiobutton(self.ConfigurationFrame,variable=self.OT,value=0,text='x')
    self.OTNCButton=Radiobutton(self.ConfigurationFrame,variable=self.OT,value=1,text='o')
    self.SoftTrailersButton=Checkbutton(self.ConfigurationFrame,variable=self.ST,text='Soft Trailers',anchor=W)
    self.LeaveTrailersButton=Checkbutton(self.ConfigurationFrame,variable=self.LT,text='Leave Tarilers',anchor=W)
    self.AccTrailersButton=Checkbutton(self.ConfigurationFrame,variable=self.AT,text='Acc on Leave',anchor=W)

    self.ConfigurationFrame.columnconfigure(0,minsize=50)
    self.ConfigurationFrame.columnconfigure(1,minsize=80)
    self.ConfigurationFrame.columnconfigure(2,minsize=50)
    self.ConfigurationFrame.columnconfigure(3,minsize=40)
    self.ConfigurationFrame.columnconfigure(4,minsize=40)
    self.ConfigurationFrame.rowconfigure(0,minsize=30)
    self.ConfigurationFrame.rowconfigure(1,minsize=34)
    self.ConfigurationFrame.rowconfigure(2,minsize=34)
    self.ConfigurationFrame.rowconfigure(3,minsize=34)
    self.ConfigurationFrame.rowconfigure(4,minsize=30)
    self.ConfigurationFrame.rowconfigure(5,minsize=30)

    self.ConfigurationLabel.grid( row=0, column=0,columnspan=2,sticky=E+W,ipadx=4,ipady=1)
    self.IMoveLabel.grid(         row=1, column=0,sticky=E+W)
    self.IMoveMenu.grid(          row=1, column=1,sticky=E+W)
    self.IStopLabel.grid(         row=2, column=0,sticky=E+W)
    self.IStopMenu.grid(          row=2, column=1,sticky=E+W)
    self.TStopLabel.grid(         row=3, column=0,sticky=E+W)
    self.TStopEntry.grid(         row=3, column=1,sticky=E+W)
    self.ApplyITButton.grid(      row=5, column=2,columnspan=3,sticky=W+E)
    self.PhaseLabel.grid(         row=0, column=2,sticky=E)
    self.Phase4Button.grid(       row=0, column=3)
    self.Phase8Button.grid(       row=0, column=4)
    self.PTLabel.grid(            row=1, column=2,sticky=E)
    self.PTNOButton.grid(         row=1, column=3)
    self.PTNCButton.grid(         row=1, column=4)
    self.NTLabel.grid(            row=2, column=2,sticky=E)
    self.NTNOButton.grid(         row=2, column=3)
    self.NTNCButton.grid(         row=2, column=4)
    self.OTLabel.grid(            row=3, column=2,sticky=E)
    self.OTNOButton.grid(         row=3, column=3)
    self.OTNCButton.grid(         row=3, column=4)
    self.SoftTrailersButton.grid( row=4, column=0,columnspan=2,sticky=W+E)
    self.LeaveTrailersButton.grid(row=5, column=0,columnspan=2,sticky=W+E)
    self.AccTrailersButton.grid(  row=4, column=2,columnspan=3,sticky=E)
    
    self.ConfigurationFrame.grid_propagate(0)
    
  def Speeds_Frame(self):
    self.Vmin, self.Vmax, self.Acc = StringVar(), StringVar(), StringVar()
    self.SpeedsFrame = Frame(self, borderwidth=2, relief=RIDGE, height=200, width=140)
    self.SpeedsFrameLabel=Label(self.SpeedsFrame, text='Speed', bg='#A0A0C0',  anchor=CENTER)
    self.VminLabel=Label(self.SpeedsFrame, text='V min:', anchor=E)
    self.VminEntry=Entry(self.SpeedsFrame, width=6, textvariable=self.Vmin, bg='#ffffff')
    self.VmaxLabel=Label(self.SpeedsFrame, text='V max:', anchor=E)
    self.VmaxEntry=Entry(self.SpeedsFrame, width=6, textvariable=self.Vmax, bg='#ffffff')
    self.AccLabel=Label(self.SpeedsFrame, text='Accel:', anchor=E)
    self.AccEntry=Entry(self.SpeedsFrame, width=6, textvariable=self.Acc, bg='#ffffff')
    self.ApplyVButton = Button (self.SpeedsFrame, text="Apply", command=self.Set_Speeds )
    self.SaveButton = Button (self.SpeedsFrame, text="Save", command=self.Save_Parameters )

    self.SpeedsFrame.rowconfigure(0,minsize=30)
    self.SpeedsFrame.rowconfigure(1,minsize=34)
    self.SpeedsFrame.rowconfigure(2,minsize=34)
    self.SpeedsFrame.rowconfigure(3,minsize=34)
    self.SpeedsFrame.rowconfigure(4,minsize=30)
    self.SpeedsFrame.rowconfigure(5,minsize=30)

    self.SpeedsFrameLabel.grid(row=0,column=0,columnspan=2,sticky=E+W,ipadx=4,ipady=1)
    self.VminLabel.grid(row=1,column=0,sticky=E+W)
    self.VminEntry.grid(row=1,column=1,sticky=E+W)
    self.VmaxLabel.grid(row=2,column=0,sticky=E+W)
    self.VmaxEntry.grid(row=2,column=1,sticky=E+W)
    self.AccLabel.grid( row=3,column=0,sticky=E+W,pady=5)
    self.AccEntry.grid( row=3,column=1,sticky=E+W)
    self.ApplyVButton.grid(row=4,column=0,columnspan=2,sticky=E+W)
    self.SaveButton.grid(row=5,column=0,columnspan=2,sticky=E+W)

    self.SpeedsFrame.grid_propagate(0)
    
  def Move_Frame(self):
    self.Steps, self.Position = StringVar(), StringVar()
    self.Steps.set('1000');  self.Position.set('0')
    self.MoveFrame = Frame(self, borderwidth=2, relief=RIDGE, height=40, width=440)

    self.LeftAccButton  = Button(self.MoveFrame, text="<<",   command=self.Go_Acc_Left,  anchor=CENTER)
    self.LeftMovButton  = Button(self.MoveFrame, text="<",    command=self.Go_Left,      anchor=CENTER)
    self.StopMovButton  = Button(self.MoveFrame, text="STOP", command=self.Stop,         anchor=CENTER)
    self.RightMovButton = Button(self.MoveFrame, text=">",    command=self.Go_Right,     anchor=CENTER)
    self.RightAccButton = Button(self.MoveFrame, text=">>",   command=self.Go_Acc_Right, anchor=CENTER)
    self.StepsLabel     =  Label(self.MoveFrame, text='Steps:', anchor=E)
    self.StepsEntry     =  Entry(self.MoveFrame, width=6, textvariable=self.Steps, bg='#ffffff')
    self.CounterButton  = Button(self.MoveFrame, textvariable=self.Position, command=self.Reset_Counter, anchor=CENTER)
    self.ExitButton     = Button(self.MoveFrame, text="Exit", command=self.Exit, anchor=CENTER)

    self.MoveFrame.columnconfigure(0,minsize=40)
    self.MoveFrame.columnconfigure(1,minsize=40)
    self.MoveFrame.columnconfigure(2,minsize=30)
    self.MoveFrame.columnconfigure(3,minsize=30)
    self.MoveFrame.columnconfigure(4,minsize=40)
    self.MoveFrame.columnconfigure(5,minsize=30)
    self.MoveFrame.columnconfigure(6,minsize=30)
    self.MoveFrame.columnconfigure(7,minsize=100)
    self.MoveFrame.columnconfigure(8,minsize=40)

    self.StepsLabel.grid(     row=0,column=0,sticky=E+W,padx=0)
    self.StepsEntry.grid(     row=0,column=1,sticky=E+W,padx=0)
    self.LeftAccButton.grid(  row=0,column=2,sticky=E+W,padx=1)
    self.LeftMovButton.grid(  row=0,column=3,sticky=E+W,padx=1)
    self.StopMovButton.grid(  row=0,column=4,sticky=E+W,padx=1)
    self.RightMovButton.grid( row=0,column=5,sticky=E+W,padx=1)
    self.RightAccButton.grid( row=0,column=6,sticky=E+W,padx=1)
    self.CounterButton.grid(  row=0,column=7,sticky=E+W,padx=0)
    self.ExitButton.grid(     row=0,column=8,sticky=E+W,padx=0)
    
    self.MoveFrame.grid_propagate(0)

  def Exit(self):
    self.M.Get_Abs_Position()
    fname='%s.pos' % self.name
    with open(fname,'w+') as f: f.write(str(self.M.Position))
    self.oops.destroy()
    
  def createWidgets(self):
    self.Communication_Frame()
    self.Status_Frame()
    self.Configuration_Frame()
    self.Speeds_Frame()
    self.Move_Frame()

    self.CommunicationFrame.grid( row=0,column=0,columnspan=4,sticky=N+E+S+W)
    self.StatusFrame.grid(        row=1,column=0,sticky=N+E+S+W)
    self.ConfigurationFrame.grid( row=1,column=1,columnspan=2,sticky=N+E+S+W)
    self.SpeedsFrame.grid(        row=1,column=3,sticky=N+E+S+W)
    self.MoveFrame.grid(          row=2,column=0,columnspan=4,sticky=N+E+S+W)

def main():
  app = Stepper(name='motor')
  app.master.title("Stepping Motor")
  app.mainloop()
  
if __name__ == "__main__":
  main()


