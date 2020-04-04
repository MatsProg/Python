#from mmap import *
import mmap
from overlay import *
from ctypes import *
#from threading import *
#import os
from struct import *
from collections import namedtuple

#from time import *
import time
import math 


def printing(slip):
    while slip[0] > 0.1 or slip[1] > 0.1 or slip[2] > 0.1 or slip[3] > 0.1:
        print(slip)

    #print(Zmienne) # wszystkie zmienne
def konwersSlip(wartosc):
        #wartosc = wartosc / 15
        wartosc = math.radians(wartosc)
       # wartosc = max(wartosc, 0)
        #wartosc = min(wartosc, 1)
        return wartosc

class Example(object):
    def __init__(self): # konstruktor
            print ('CREATED')
            self.name = 'OVERLAY'
            self.shm = mmap.mmap(0, 1024, "Local\\acpmf_physics")     
            self.Liczby = namedtuple('Liczby',
                                'packetId gas brake fuel gear rpms steerAngle speedKmh velocity1 velocity2 velocity3 accG1 accG2 accG3 wheelSlipFL wheelSlipFR wheelSlipRL wheelSlipRR wheelLoadFL wheelLoadFR wheelLoadRL wheelLoadRR wheelsPressureFL wheelsPressureFR wheelsPressureRL wheelsPressureRR wheelAngularSpeedFL wheelAngularSpeedFR wheelAngularSpeedRL wheelAngularSpeedRR')
            self.ovl = Overlay()

    
    def main(self):        
            # najpierw musimy ustawic obiekt shm na poczatek
        self.shm.seek(0)  # to mowi zeby zaczac czytac od 0
        bajty = self.shm.read(120) # obiekt shm teraz wskazuje na +120 znakow


        Zmienne = self.Liczby._make(unpack('ifffiiffffffffffffffffffffffff', bajty))
            
        wheelSlip = konwersSlip(getattr(Zmienne, 'wheelSlipFL')), konwersSlip(getattr(Zmienne, 'wheelSlipFR')), konwersSlip(getattr(Zmienne, 'wheelSlipRL')), konwersSlip(getattr(Zmienne, 'wheelSlipRR'))
       # printing(wheelSlip)
        print(wheelSlip)
            
        
        self.ovl.updateWheelSlip(wheelSlip[2], wheelSlip[3], wheelSlip[0], wheelSlip[1])
        

ex = Example() # tutaj sie wykona funkcja __init__                                                                                                        
while(True):
    if __name__ == '__main__':        
        #time.sleep(1)
        ex.main()
        
        

"""
if __name__ == '__main__':
    Example().main()
        
    
def Graph():
    win = GraphWin("My Window", 500, 500)
    win.setBackground("blue")
    win.getMouse()
    win.close()

Zmienne = Liczby(packetId, gas, brake, fuel, gear, rpms, steerAngle, speedKmh, velocity1, velocity2,
                             velocity3, accG1, accG2, accG3, wheelSlipFL, wheelSlipFR, wheelSlipRL, wheelSlipRR,
                             wheelLoadFL, wheelLoadFR, wheelLoadRL, wheelLoadRR, wheelsPressureFL, wheelsPressureFR,
                             wheelsPressureRL, wheelsPressureRR, wheelAngularSpeedFL, wheelAngularSpeedFR,
                             wheelAngularSpeedRL, wheelAngularSpeedRR)

"""
