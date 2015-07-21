__author__ = 'mark'
#pi
import math
def get_pi():
    r = 1
    degree = 90
    num = 4
    i = 1
    height = 1.0
    while height > 0.00001:
        height = float(math.sin(math.radians(degree)))
        one_area = 0.5 * r * r * height
        t_area = one_area * num
        num = float(num * 2)
        degree = float(degree / 2)

    return t_area


print get_pi()