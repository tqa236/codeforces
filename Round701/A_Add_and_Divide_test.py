import unittest

from A_Add_and_Divide import func


class Test(unittest.TestCase):
    # def test_1(self):
    #     self.assertEqual(func(9, 2), 4)

    # def test_2(self):
    #     self.assertEqual(func(1337, 1), 9)

    # def test_3(self):
    #     self.assertEqual(func(1, 1), 2)

    def test_4(self):
        self.assertEqual(func(50000000, 4), 12)


if __name__ == "__main__":
    unittest.main()