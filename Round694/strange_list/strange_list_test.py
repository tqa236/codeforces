import unittest
from strange_list import strange_list


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(strange_list([12], 2), 36)

    def test_2(self):
        self.assertEqual(strange_list([4, 6, 8, 2], 2), 44)


if __name__ == "__main__":
    unittest.main()