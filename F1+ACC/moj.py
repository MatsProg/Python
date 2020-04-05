import mmap
from struct import *
from collections import namedtuple


class mmapbity(object):
    def __init__(self):
        print('Odbieranie bitow')
        self.shm = mmap.mmap(0, 1024, "Local\\acpmf_physics")
        self.Liczby = namedtuple('Liczby',
                                 'packetId gas brake fuel gear rpms steerAngle speedKmh velocity1 velocity2 velocity3 accG1 accG2 accG3 wheelSlipFL wheelSlipFR wheelSlipRL wheelSlipRR wheelLoadFL wheelLoadFR wheelLoadRL wheelLoadRR wheelsPressureFL wheelsPressureFR wheelsPressureRL wheelsPressureRR wheelAngularSpeedFL wheelAngularSpeedFR wheelAngularSpeedRL wheelAngularSpeedRR')
        self.shm.seek(0)
        self.bajty = self.shm.read(120)  # obiekt shm teraz wskazuje na +120 znakow
        self.Zmienne = self.Liczby._make(unpack('ifffiiffffffffffffffffffffffff', self.bajty))


obiekt1 = mmapbity()
