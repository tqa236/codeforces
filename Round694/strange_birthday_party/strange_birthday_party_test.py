import unittest
from strange_birthday_party import strange_birthday_party


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(strange_birthday_party([2, 3, 4, 3, 2], [3, 5, 12, 20]), 30)

    def test_2(self):
        self.assertEqual(
            strange_birthday_party([5, 4, 3, 2, 1], [10, 40, 90, 160, 250]), 190
        )

    def test_3(self):
        self.assertEqual(
            strange_birthday_party([5, 5, 4, 3, 2, 1], [10, 40, 90, 160, 250]), 280
        )

    def test_4(self):
        self.assertEqual(
            strange_birthday_party([5, 5, 4, 3, 2], [10, 40, 90, 160, 250]), 270
        )

    def test_5(self):
        self.assertEqual(
            strange_birthday_party([5, 5, 5, 5, 5, 5], [10, 40, 90, 160, 250]), 800
        )

    def test_6(self):
        self.assertEqual(strange_birthday_party([2], [10, 40, 90, 160, 250]), 10)

    def test_7(self):
        self.assertEqual(strange_birthday_party([2], [10]), 10)

    def test_8(self):
        self.assertEqual(
            strange_birthday_party([1, 1, 1, 1, 1], [10, 40, 90, 160, 250]), 50
        )


if __name__ == "__main__":
    unittest.main()