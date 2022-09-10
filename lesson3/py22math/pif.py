from .triangle import Triangle
import math


class PifTriangle(Triangle):
    has_90_deg_corner = True

    def count_gip(self, katet_1, katet_2):
        gip = math.sqrt(katet_1 ** 2 + katet_2 ** 2)
        return gip
