import unittest

from painting_the_array_ii import painting_the_array_ii


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(painting_the_array_ii([1, 2, 3, 1, 2, 2]), 4)

    def test_2(self):
        self.assertEqual(painting_the_array_ii([1, 2, 1, 2, 1, 2, 1]), 2)

    def test_3(self):
        self.assertEqual(painting_the_array_ii([1, 2, 1, 2, 1, 2, 1, 1]), 2)


if __name__ == "__main__":
    unittest.main()