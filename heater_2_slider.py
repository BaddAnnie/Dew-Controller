import Tkinter
#from Adafruit_PWM_Servo_Driver import PWM

def setPulse(channel, percent):
    print(channel, percent)
    pwm.setPWM(channel,0,int(float(percent)*4095))

root = Tkinter.Tk( )
#pwm = PWM(0x40, debug=True)

#pwm.setPWMFreq(60)

Tkinter.Label(root, text="Objective Dew",anchor=Tkinter.W,background="red").grid(row=0)
Tkinter.Label(root, text="Eyepiece Dew",anchor=Tkinter.W,background="red").grid(row=1)

Tkinter.Scale(root, from_=0, to=1, background="red",orient=Tkinter.HORIZONTAL,resolution=.01,width = 50,sliderlength = 40).grid(row = 0, column = 1)
Tkinter.Scale(root, from_=0, to=1, background="red",orient=Tkinter.HORIZONTAL,resolution=.01,width = 50,sliderlength = 40).grid(row = 1, column = 1)

#command=lambda x:setPulse(0,x)

root.mainloop( )
