import unittest
from strange_partition import strange_partition


class Test(unittest.TestCase):
    def test_1(self):
        min_bound, max_bound = strange_partition([3, 6, 9], 3)
        self.assertEqual(min_bound, 6)
        self.assertEqual(max_bound, 6)

    def test_2(self):
        min_bound, max_bound = strange_partition([6, 4, 11], 3)
        self.assertEqual(min_bound, 7)
        self.assertEqual(max_bound, 8)


if __name__ == "__main__":
    unittest.main()