import unittest
from cards_for_friends import cards_for_friends


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(cards_for_friends(2, 2, 3), True)

    def test_2(self):
        self.assertEqual(cards_for_friends(3, 3, 2), False)

    def test_3(self):
        self.assertEqual(cards_for_friends(5, 10, 2), True)

    def test_4(self):
        self.assertEqual(cards_for_friends(1, 4, 4), True)


if __name__ == "__main__":
    unittest.main()
