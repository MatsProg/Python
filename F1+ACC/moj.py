import mmap
from struct import *
from collections import namedtuple
import math

def konwersSlip(wartosc):
    wartosc = wartosc / 5
    wartosc = max(wartosc, 0)
    wartosc = min(wartosc, 1)
    math.radians(wartosc)
    # pow(wartosc, (wartosc+10)**10)
    # round(wartosc,2)
    # pow(wartosc,wartosc)
    # "{:.2f}".format(wartosc)
    return wartosc
class mmapbity:
    def odbieranieBitow1(self):

        self.shm = mmap.mmap(0, 1024, "Local\\acpmf_physics")
        self.Liczby = namedtuple('Liczby',
                                 'packetId gas brake fuel gear rpms steerAngle speedKmh velocity1 velocity2 velocity3 accG1 accG2 accG3 wheelSlipFL wheelSlipFR wheelSlipRL wheelSlipRR wheelLoadFL wheelLoadFR wheelLoadRL wheelLoadRR wheelsPressureFL wheelsPressureFR wheelsPressureRL wheelsPressureRR wheelAngularSpeedFL wheelAngularSpeedFR wheelAngularSpeedRL wheelAngularSpeedRR')
        self.shm.seek(0)
        self.bajty = self.shm.read(120)  # obiekt shm teraz wskazuje na +120 znakow
        self.Zmienne = self.Liczby._make(unpack('ifffiiffffffffffffffffffffffff', self.bajty))
        self.wheelSlip = pow(konwersSlip(getattr(self.Zmienne, 'wheelSlipFL')),3), pow(konwersSlip(getattr(self.Zmienne, 'wheelSlipFR')),3), pow(konwersSlip(getattr(self.Zmienne, 'wheelSlipRL')),2), pow(konwersSlip(getattr(self.Zmienne, 'wheelSlipRR')), 2)
        print('Odbieranie bitow z funkcji')
        return self.wheelSlip

obiekt1 = mmapbity()
obiekt1.odbieranieBitow1()
