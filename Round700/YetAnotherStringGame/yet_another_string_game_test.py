import unittest

from yet_another_string_game import yet_another_string_game


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(yet_another_string_game("a"), "b")

    def test_2(self):
        self.assertEqual(yet_another_string_game("bb"), "az")

    def test_3(self):
        self.assertEqual(yet_another_string_game("bbbb"), "azaz")


if __name__ == "__main__":
    unittest.main()
