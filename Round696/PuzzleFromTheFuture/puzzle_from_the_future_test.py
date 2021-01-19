import unittest

from puzzle_from_the_future import puzzle_from_the_future


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(puzzle_from_the_future(1, "0"), "1")

    def test_2(self):
        self.assertEqual(puzzle_from_the_future(3, "011"), "110")

    def test_3(self):
        self.assertEqual(puzzle_from_the_future(3, "110"), "100")

    def test_4(self):
        self.assertEqual(puzzle_from_the_future(6, "111000"), "101101")


if __name__ == "__main__":
    unittest.main()