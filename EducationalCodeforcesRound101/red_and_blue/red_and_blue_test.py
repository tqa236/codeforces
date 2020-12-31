import unittest
from red_and_blue import red_and_blue


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(red_and_blue([6, -5, 7, -3], [2, 3, -4]), 13)

    def test_2(self):
        self.assertEqual(red_and_blue([1, 1], [10, -3, 2, 2]), 13)

    def test_3(self):
        self.assertEqual(red_and_blue([-1, -2, -3, -4, -5], [-1, -2, -3, -4, -5]), 0)

    def test_4(self):
        self.assertEqual(red_and_blue([0], [0]), 0)


if __name__ == "__main__":
    unittest.main()