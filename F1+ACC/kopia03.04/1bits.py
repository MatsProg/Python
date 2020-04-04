import mmmap

class Bits(object)
    def __init__(self):
        print('CREATED')
        self.name = 'OVERLAY'
        self.shm = mmap.mmap(0, 1024, "Local\\acpmf_physics")
        self.Liczby = namedtuple('Liczby',
                                 'packetId gas brake fuel gear rpms steerAngle speedKmh velocity1 velocity2 velocity3 accG1 accG2 accG3 wheelSlipFL wheelSlipFR wheelSlipRL wheelSlipRR wheelLoadFL wheelLoadFR wheelLoadRL wheelLoadRR wheelsPressureFL wheelsPressureFR wheelsPressureRL wheelsPressureRR wheelAngularSpeedFL wheelAngularSpeedFR wheelAngularSpeedRL wheelAngularSpeedRR')
        self.ovl = Overlay()