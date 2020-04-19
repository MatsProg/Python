import math


class Obliczenia:

    def konwersSlip(wartosc, x):
        wartosc = wartosc / 5
        wartosc = max(wartosc, 0)
        wartosc = min(wartosc, 1)
        math.radians(wartosc)
        return pow(wartosc, x)

