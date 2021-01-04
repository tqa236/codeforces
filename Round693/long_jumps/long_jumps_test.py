import unittest
from long_jumps import long_jumps


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(long_jumps([7, 3, 1, 2, 3]), 7)

    def test_2(self):
        self.assertEqual(long_jumps([2, 1000, 2, 3, 995, 1]), 1000)

    def test_3(self):
        self.assertEqual(long_jumps([1, 1, 1, 1, 1]), 5)

    def test_4(self):
        self.assertEqual(long_jumps([2, 1, 4]), 6)


if __name__ == "__main__":
    unittest.main()