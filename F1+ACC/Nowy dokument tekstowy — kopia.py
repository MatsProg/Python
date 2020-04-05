import mmap
from overlay import *
from struct import *
from collections import namedtuple
import math
import time

def konwersSlip(wartosc):
        wartosc = wartosc / 5
        wartosc = max(wartosc, 0)
        wartosc = min(wartosc, 1)
        math.radians(wartosc)
        #pow(wartosc, (wartosc+10)**10)
       # round(wartosc,2)
        #pow(wartosc,wartosc)
       # "{:.2f}".format(wartosc)
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
            
        wheelSlip = pow(konwersSlip(getattr(Zmienne, 'wheelSlipFL')),3), pow(konwersSlip(getattr(Zmienne, 'wheelSlipFR')),3), pow(konwersSlip(getattr(Zmienne, 'wheelSlipRL')),2), pow(konwersSlip(getattr(Zmienne, 'wheelSlipRR')), 2)

            
        
        self.ovl.updateWheelSlip(wheelSlip[2], wheelSlip[3], wheelSlip[0], wheelSlip[1]) #[FL, FR, RL, RR]

        wheelSlipRR = getattr(Zmienne, 'wheelSlipRR')
        wheelSlipRL = getattr(Zmienne, 'wheelSlipRL')
        wheelSlipFL = getattr(Zmienne, 'wheelSlipFL')
        wheelSlipFR = getattr(Zmienne, 'wheelSlipFR')
        if wheelSlipRR != 0 or wheelSlipRL != 0 or wheelSlipFL != 0 or wheelSlipRL != 0:
            print(wheelSlip)#print

            #print(Zmienne)
ex = Example() # tutaj sie wykona funkcja __init__                                                                                                        
while(True):
    if __name__ == '__main__':        
        #time.sleep(1)
        ex.main()
