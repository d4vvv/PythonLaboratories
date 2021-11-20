class Complex:
    re = 0
    im = 0

    def __init__(self, re_, im_=0.0):
        self.re = re_
        self.im = im_

    def add(self, complex2):
        return Complex(self.re + complex2.re, self.im + complex2.im)

    def subtract(self, complex2):
        return Complex(self.re - complex2.re, self.im - complex2.im)

    def multiply(self, complex2):
        return Complex(self.re * complex2.re - self.im * complex2.im, self.im * complex2.re + self.re * complex2.im)

    def divide(self, complex2):
        divisor = complex2.multiply(Complex(complex2.re, -complex2.im)).re
        intermediate = self.multiply(Complex(complex2.re, -complex2.im))
        return Complex(intermediate.re/divisor, intermediate.im/divisor)

    def print(self):
        if self.im < 0:
            return str(self.re) + " - " + str(abs(self.im)) + "i"
        else:
            return str(self.re) + " + " + str(self.im) + "i"


c1 = Complex(10, 2)
c2 = Complex(2, -2)

c3 = c1.divide(c2)
print(c3.print())
