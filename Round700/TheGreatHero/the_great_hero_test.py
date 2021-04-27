import unittest

from the_great_hero import the_great_hero


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(the_great_hero(3, 17, [2], [16]), "YES")


if __name__ == "__main__":
    unittest.main()
