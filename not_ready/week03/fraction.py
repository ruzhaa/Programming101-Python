class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + \
                        self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        if new_numerator == new_denominator:
            return '1'
        return self.simplify(Fraction(new_numerator, new_denominator))

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - \
                        self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        if new_numerator == new_denominator:
            return '1'
        if new_numerator == 0:
            return '0'
        return self.simplify(Fraction(new_numerator, new_denominator))

    def __mul__(self, other):
        return self.simplify(Fraction(self.numerator * other.numerator, \
                        self.denominator * other.denominator))

    def __eq__(self, other):
        return self.simplify(self) == self.simplify(other)

# za namirane na NOD
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def simplify(self, fraction):
        nod = self.gcd(fraction.numerator, fraction.denominator)
        fraction.numerator /= nod
        fraction.denominator /= nod
        return str(Fraction(int(fraction.numerator), int(fraction.denominator)))
