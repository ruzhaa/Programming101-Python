import unittest
from fraction import Fraction


class TestFraction(unittest.TestCase):

    def setUp(self):
        self.fraction = Fraction(1, 2)

    def test_fraction_init(self):
        self.assertEqual(self.fraction.numerator, 1)
        self.assertEqual(self.fraction.denominator, 2)

    def test_fraction_str(self):
        self.assertEqual(str(self.fraction), \
      "{} / {}". format(self.fraction.numerator, self.fraction.denominator))


    # def test_fraction_add(self, other):
    #     pass


if __name__ == '__main__':
    unittest.main()
