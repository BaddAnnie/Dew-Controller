import Tkinter
from Adafruit_PWM_Servo_Driver import PWM

def setPulse(channel, percent):
    print(channel, percent)
    pwm.setPWM(channel,0,int(float(percent)*4095))

root = Tkinter.Tk( )
pwm = PWM(0x40, debug=True)

pwm.setPWMFreq(60)

Tkinter.Label(root, text="Primary Dew").grid(row=0)
Tkinter.Label(root, text="Secondary Dew").grid(row=1)

Tkinter.Scale(root, from_=0, to=1, orient=Tkinter.HORIZONTAL,resolution=.01,command=lambda x:setPulse(0,x)).grid(row = 0, column = 1)
Tkinter.Scale(root, from_=0, to=1, orient=Tkinter.HORIZONTAL,resolution=.01).grid(row = 1, column = 1)

root.mainloop( )
