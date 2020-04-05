
from overlay import *
from struct import *
from collections import namedtuple
import math
import time
from moj import *

#odbieranieBitow = mmapbity()
#start = odbieranieBitow.odbieranieBitow1()
#WH = odbieranieBitow.odbieranieBitow1()
#Wheel = odbieranieBitow.wheelSlip




class Example(mmapbity):
    def __init__(self): # konstruktor
        self.ovl = Overlay()
    def main(self):
        AA = Example.odbieranieBitow1() ######### wheel slip nie dziala. nie odbiera danych, probuje z dziedziczeniem

        self.wheelSlip = Example.odbieranieBitow1.
        #print('start main')
        self.ovl.updateWheelSlip(self.wheelSlip[2], self.wheelSlip[3], self.wheelSlip[0], self.wheelSlip[1])  # [FL, FR, RL, RR]
        #self.ovl.updateWheelSlip(odbieranieBitow.wheelSlip[2], odbieranieBitow.wheelSlip[3], odbieranieBitow.wheelSlip[0], odbieranieBitow.wheelSlip[1])  # [FL, FR, RL, RR]
        print(self.wheelSlip)
Obiekta = Example()
Obiekta.main()
ex = Example() # tutaj sie wykona funkcja __init__
while(True):
    if __name__ == '__main__':
        #time.sleep(1)
        ex.main()