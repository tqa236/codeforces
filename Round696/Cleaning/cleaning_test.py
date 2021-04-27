import unittest

from cleaning import cleaning


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(cleaning([2100, 1900, 1600, 3000, 1600]), True)

    def test_2(self):
        self.assertEqual(cleaning([1, 2, 1]), True)

    def test_3(self):
        self.assertEqual(cleaning([1, 4, 1, 1, 3]), True)

    def test_4(self):
        self.assertEqual(cleaning([1, 4, 3, 1, 1]), True)

    def test_5(self):
        self.assertEqual(cleaning([1, 10, 1, 1, 5, 1, 5]), True)

    def test_6(self):
        self.assertEqual(cleaning([1, 10, 1, 1, 5, 1, 1, 1, 5]), False)

    def test_7(self):
        self.assertEqual(cleaning([1, 3]), False)

    def test_8(self):
        self.assertEqual(cleaning([2, 2, 2, 1, 3]), True)

    def test_9(self):
        self.assertEqual(cleaning([1]), False)

    def test_10(self):
        self.assertEqual(cleaning([1, 2, 2]), False)

    def test_11(self):
        self.assertEqual(cleaning([1, 2, 5]), False)

    def test_12(self):
        self.assertEqual(cleaning([1, 2, 3]), True)

    def test_13(self):
        self.assertEqual(cleaning([2, 9, 8, 1, 1, 3]), False)

    def test_14(self):
        self.assertEqual(cleaning([2, 9, 8, 3, 1, 1]), True)


if __name__ == "__main__":
    unittest.main()
