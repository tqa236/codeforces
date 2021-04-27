import unittest
from correct_placement import correct_placement


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(correct_placement([(3, 4), (4, 5), (3, 3)]), [-1, 1, -1])

    def test_2(self):
        self.assertEqual(correct_placement([(1, 3), (2, 2), (1, 3)]), [-1, -1, -1])

    def test_3(self):
        self.assertEqual(
            correct_placement([(2, 2), (1, 3), (3, 6), (4, 5)]), [-1, -1, 2, 2]
        )


if __name__ == "__main__":
    unittest.main()
