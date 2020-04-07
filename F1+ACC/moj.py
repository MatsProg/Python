import mmap
from struct import *
from collections import namedtuple
import math


class Obliczenia:

    def konwersSlip(wartosc, x):
        wartosc = wartosc / 5
        wartosc = max(wartosc, 0)
        wartosc = min(wartosc, 1)
        math.radians(wartosc)
        # pow(wartosc, (wartosc+10)**10)
        # round(wartosc,2)
        # pow(wartosc,wartosc)
        # "{:.2f}".format(wartosc)
        return pow(wartosc, x)


#obiekt1 = Obliczenia()
#obiekt1.konwersSlip(x)
