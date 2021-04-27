import unittest
from fair_division import is_possible


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_possible([1, 1]), True)

    def test_2(self):
        self.assertEqual(is_possible([1, 2]), False)

    def test_3(self):
        self.assertEqual(is_possible([1, 2, 1, 2]), True)

    def test_4(self):
        self.assertEqual(is_possible([2, 2, 2]), False)

    def test_5(self):
        self.assertEqual(is_possible([2, 1, 2]), False)

    def test_6(self):
        self.assertEqual(is_possible([2]), False)

    def test_7(self):
        self.assertEqual(is_possible([1, 2, 1, 2, 2]), True)


if __name__ == "__main__":
    unittest.main()
