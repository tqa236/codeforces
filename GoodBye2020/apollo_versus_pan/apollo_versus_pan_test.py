import unittest
from apollo_versus_pan import apollo_versus_pan


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(apollo_versus_pan([1, 7]), 128)

    def test_2(self):
        self.assertEqual(
            apollo_versus_pan(
                [
                    536870912,
                    536870911,
                    1152921504606846975,
                    1152921504606846974,
                    1152921504606846973,
                ]
            ),
            264880351,
        )

    def test_3(self):
        self.assertEqual(apollo_versus_pan([0]), 0)

    def test_4(self):
        self.assertEqual(apollo_versus_pan([1]), 1)

    def test_5(self):
        self.assertEqual(
            apollo_versus_pan([1, 12, 123, 1234, 12345, 123456]), 502811676
        )


if __name__ == "__main__":
    unittest.main()
