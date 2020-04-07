
from overlay import *
from struct import *
from collections import namedtuple
import math
import time
from moj import *
import mmap
from struct import *
from collections import namedtuple
import math

#odbieranieBitow = mmapbity()
#start = odbieranieBitow.odbieranieBitow1()
#WH = odbieranieBitow.odbieranieBitow1()
#Wheel = odbieranieBitow.wheelSlip
mmapBi = mmapbity()
mmapBi.odbieranieBitow1()
wheelSlipp = mmapBi.wheelSlip
x = 0


class Example():
    def __init__(self): # konstruktor
        self.ovl = Overlay()
    def main(self):
       # AA = Example.odbieranieBitow1(x)
        pass


        #print('start main')
        #self.ovl.updateWheelSlip(self.wheelSlip[2], self.wheelSlip[3], self.wheelSlip[0], self.wheelSlip[1])  # [FL, FR, RL, RR]
        self.ovl.updateWheelSlip(wheelSlipp[2], wheelSlipp[3], wheelSlipp[0], wheelSlipp[1])  # [FL, FR, RL, RR]
        #print(mmapBi.wheelSlip)
        print(wheelSlipp)
Obiekt = Example()
#Obiekt.main()
#ex = Example() # tutaj sie wykona funkcja __init__
while(True):
    if __name__ == '__main__':
        #time.sleep(1)
        Obiekt.main()