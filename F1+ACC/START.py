import mmap
from overlay import *
from struct import *
from collections import namedtuple
from obliczenia import Obliczenia as Ob  #importuje plik
import math
import time


class Example(object):
    def __init__(self):
        print('PROCESS CREATED')
        self.name = 'OVERLAY'
        self.mmapPhysic = mmap.mmap(0, 1024, "Local\\acpmf_physics")
        self.bityTuple = namedtuple('Liczby',
                                    'packetId gas brake fuel gear rpms steerAngle speedKmh velocity1 velocity2 velocity3 accG1 accG2 accG3 wheelSlipFL wheelSlipFR wheelSlipRL wheelSlipRR wheelLoadFL wheelLoadFR wheelLoadRL wheelLoadRR wheelsPressureFL wheelsPressureFR wheelsPressureRL wheelsPressureRR wheelAngularSpeedFL wheelAngularSpeedFR wheelAngularSpeedRL wheelAngularSpeedRR')
        self.ovl = Overlay()

    def bits(self):  #Odbiera bytes
        self.mmapPhysic.seek(0)  # to mowi zeby zaczac czytac od 0
        self.bytesValue = self.mmapPhysic.read(120)  # obiekt wskazuje na +120 znakow
        self.unpackTuple = self.bityTuple._make(unpack('ifffiiffffffffffffffffffffffff', self.bytesValue))
        self.wheelSlip = Ob.konwersSlip(getattr(self.unpackTuple, 'wheelSlipFL'), 3), Ob.konwersSlip(getattr(self.unpackTuple, 'wheelSlipFR'), 3), Ob.konwersSlip(getattr(self.unpackTuple, 'wheelSlipRL'),2), Ob.konwersSlip(getattr(self.unpackTuple, 'wheelSlipRR'), 2)

    def main(self):
        self.ovl.updateWheelSlip(self.wheelSlip[2], self.wheelSlip[3], self.wheelSlip[0], self.wheelSlip[1])  # [FL, FR, RL, RR]


ex = Example()
while (True):
    if __name__ == '__main__':
        # time.sleep(1)
        ex.bits()
        ex.main()
