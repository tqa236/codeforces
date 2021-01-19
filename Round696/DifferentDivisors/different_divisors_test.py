import unittest

from different_divisors import different_divisors


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(different_divisors(1), 6)

    def test_2(self):
        self.assertEqual(different_divisors(2), 15)

    def test_3(self):
        self.assertEqual(different_divisors(3), 55)

    def test_4(self):
        self.assertEqual(different_divisors(100), 21311)


if __name__ == "__main__":
    unittest.main()