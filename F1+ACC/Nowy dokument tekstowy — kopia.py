import mmap
from overlay import *
from struct import *
from collections import namedtuple
import math
import time
from moj import Obliczenia as Ob


def konwersSlip1(wartosc):
    wartosc = wartosc / 5
    wartosc = max(wartosc, 0)
    wartosc = min(wartosc, 1)
    math.radians(wartosc)
    # pow(wartosc, (wartosc+10)**10)
    # round(wartosc,2)
    # pow(wartosc,wartosc)
    # "{:.2f}".format(wartosc)
    return wartosc


class Example(object):
    def __init__(self):  # konstruktor
        print('CREATED')
        self.name = 'OVERLAY'
        self.mmapPhysic = mmap.mmap(0, 1024, "Local\\acpmf_physics")
        self.bityTuple = namedtuple('Liczby',
                                    'packetId gas brake fuel gear rpms steerAngle speedKmh velocity1 velocity2 velocity3 accG1 accG2 accG3 wheelSlipFL wheelSlipFR wheelSlipRL wheelSlipRR wheelLoadFL wheelLoadFR wheelLoadRL wheelLoadRR wheelsPressureFL wheelsPressureFR wheelsPressureRL wheelsPressureRR wheelAngularSpeedFL wheelAngularSpeedFR wheelAngularSpeedRL wheelAngularSpeedRR')
        self.ovl = Overlay()

    def bits(self):
        self.mmapPhysic.seek(0)  # to mowi zeby zaczac czytac od 0
        self.bytesValue = self.mmapPhysic.read(120)  # obiekt shm teraz wskazuje na +120 znakow
        self.unpackTuple = self.bityTuple._make(unpack('ifffiiffffffffffffffffffffffff', self.bytesValue))
        self.wheelSlip = Ob.konwersSlip(getattr(self.unpackTuple, 'wheelSlipFL'),3), Ob.konwersSlip(getattr(self.unpackTuple, 'wheelSlipFR'),3), Ob.konwersSlip(getattr(self.unpackTuple, 'wheelSlipRL'),2), Ob.konwersSlip(getattr(self.unpackTuple, 'wheelSlipRR'),2)

   # Ob.konwersSlip()
    def main(self):
        # najpierw musimy ustawic obiekt shm na poczatek

        self.ovl.updateWheelSlip(self.wheelSlip[2], self.wheelSlip[3], self.wheelSlip[0],
                                 self.wheelSlip[1])  # [FL, FR, RL, RR]

    #  wheelSlipRR = getattr(Zmienne, 'wheelSlipRR')
    #  wheelSlipRL = getattr(Zmienne, 'wheelSlipRL')
    #   wheelSlipFL = getattr(Zmienne, 'wheelSlipFL')
    #  wheelSlipFR = getattr(Zmienne, 'wheelSlipFR')
    #  if wheelSlipRR != 0 or wheelSlipRL != 0 or wheelSlipFL != 0 or wheelSlipRL != 0:
    #    print(wheelSlip)#print

    # print(Zmienne)


ex = Example()  # tutaj sie wykona funkcja __init__
while (True):
    if __name__ == '__main__':
        # time.sleep(1)
        ex.bits()
        ex.main()
