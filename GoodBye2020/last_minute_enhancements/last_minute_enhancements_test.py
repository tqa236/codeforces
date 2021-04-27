import unittest
from last_minute_enhancements import last_minute_enhancements


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(last_minute_enhancements([1, 2, 2, 2, 5, 6]), 5)

    def test_2(self):
        self.assertEqual(last_minute_enhancements([4, 4]), 2)

    def test_3(self):
        self.assertEqual(last_minute_enhancements([1, 1, 1, 2, 2, 2]), 3)


if __name__ == "__main__":
    unittest.main()
