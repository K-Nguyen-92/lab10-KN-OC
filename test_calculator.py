# https://github.com/K-Nguyen-92/lab10-KN-OC
# Partner 1: Khoa Nguyen
# Partner 2: Octavia Chambers

import unittest

from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-4, 2), -2)

    def test_subtract(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(8, 3), 5)
        self.assertEqual(sub(2, 7), -5)

    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(12, 2), 24)
        self.assertEqual(multiply(5, 7), 35)

    def test_divide(self):
        self.assertEqual(divide(3, 12), 4)
        self.assertEqual(divide(3, 36), 12)
        self.assertEqual(divide(4, 128), 32)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(log(2, 8), 3.0)
        self.assertAlmostEqual(log(10, 100), 2.0)
        self.assertAlmostEqual(log(3, 27), 3.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(12, 5), 13.0)
        self.assertAlmostEqual(hypotenuse(6, 8), 10.0)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(25), 5.0)
        self.assertAlmostEqual(square_root(144), 12.0)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
