import unittest
from bovine_dilemma import bovine_dilemma


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(bovine_dilemma([1, 2, 4, 5]), 4)

    def test_2(self):
        self.assertEqual(bovine_dilemma([50]), 0)

    def test_3(self):
        self.assertEqual(bovine_dilemma([1, 2, 4, 8, 16, 32]), 15)


if __name__ == "__main__":
    unittest.main()
