import unittest
from even_odd_game import even_odd_game


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(even_odd_game([5, 2, 7, 3]), "Bob")


if __name__ == "__main__":
    unittest.main()
