import unittest

from painting_the_array_i import painting_the_array_i


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(painting_the_array_i([1, 1, 2, 2, 3, 3, 3]), 6)

    def test_2(self):
        self.assertEqual(painting_the_array_i([1, 2, 3, 4, 5, 6, 7]), 7)

    def test_3(self):
        self.assertEqual(painting_the_array_i([1, 2, 3, 4, 5, 6, 7, 7]), 8)

    def test_4(self):
        self.assertEqual(painting_the_array_i([1, 1, 1, 1]), 2)

    def test_5(self):
        self.assertEqual(painting_the_array_i([1, 1, 2, 1, 1]), 4)

    def test_6(self):
        self.assertEqual(painting_the_array_i([1, 1, 2, 1, 2, 3, 4]), 7)

    def test_7(self):
        self.assertEqual(painting_the_array_i([1, 1, 2, 1, 2, 3, 4, 4]), 8)

    def test_8(self):
        self.assertEqual(painting_the_array_i([1, 1, 2, 3, 4, 3, 4, 2, 1]), 9)

    def test_9(self):
        self.assertEqual(painting_the_array_i([1, 1, 2, 3, 4, 1, 1]), 7)

    def test_10(self):
        self.assertEqual(painting_the_array_i([1]), 1)

    def test_11(self):
        self.assertEqual(painting_the_array_i([1, 1]), 2)

    def test_12(self):
        self.assertEqual(painting_the_array_i([1, 1, 2, 3, 4, 5, 1, 1]), 8)

    def test_13(self):
        self.assertEqual(painting_the_array_i(list(range(1000))), 1000)

    def test_14(self):
        self.assertEqual(painting_the_array_i([1, 2] * 1000), 2000)

    def test_15(self):
        self.assertEqual(painting_the_array_i([1, 1, 2, 2] * 1000), 4000)

    def test_16(self):
        self.assertEqual(painting_the_array_i([1, 1, 2, 3, 2, 4, 5, 2, 2]), 9)

    def test_17(self):
        self.assertEqual(painting_the_array_i([1, 1, 2, 3, 2, 4, 3, 2, 2]), 9)

    def test_18(self):
        self.assertEqual(painting_the_array_i([1, 1, 2, 3, 2, 4, 3, 3, 3, 2, 2]), 10)

    def test_19(self):
        self.assertEqual(painting_the_array_i([1, 1, 2, 3, 3, 2, 4, 3, 2, 2]), 10)

    def test_20(self):
        self.assertEqual(painting_the_array_i([1, 1, 2, 3, 3, 2, 4, 3, 4, 4]), 10)


if __name__ == "__main__":
    unittest.main()