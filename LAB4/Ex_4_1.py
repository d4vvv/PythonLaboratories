import numpy
import math


def roots(a, b, c):
    d = pow(b, 2) - (4 * a * c)
    d_sqrt = math.sqrt(abs(d))

    if d > 0:
        print((-b + d_sqrt) / (2 * a))
        print((-b - d_sqrt) / (2 * a))

    elif d == 0:
        print(-b / (2 * a))

    else:
        print(str(-b / (2 * a)) + " + i" + str(d_sqrt))
        print(str(-b / (2 * a)) + " - i" + str(d_sqrt))


a = 4
b = 2
c = -3

roots(a, b, c)
print(numpy.roots([a, b, c]))  # verification
