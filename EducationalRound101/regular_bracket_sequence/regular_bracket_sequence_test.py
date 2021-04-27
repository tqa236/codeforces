import unittest
from regular_bracket_sequence import is_regular_sequence


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_regular_sequence("()"), True)

    def test_2(self):
        self.assertEqual(is_regular_sequence("(?)"), False)

    def test_3(self):
        self.assertEqual(is_regular_sequence("(??)"), True)

    def test_4(self):
        self.assertEqual(is_regular_sequence("??()"), True)

    def test_5(self):
        self.assertEqual(is_regular_sequence(")?(?"), False)

    def test_6(self):
        self.assertEqual(is_regular_sequence("?)?("), False)


if __name__ == "__main__":
    unittest.main()
