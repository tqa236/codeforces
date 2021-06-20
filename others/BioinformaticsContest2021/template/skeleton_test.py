import unittest
import hypothesis.strategies as st
from hypothesis import given
from {exercise_name} import Solution


class Test(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.{method}(), True)

    @given(st.lists(st.integers(), min_size=1), st.lists(st.integers()))
    def test_random(self, x, y):
        solution = Solution()
        self.assertEqual(solution.{method}(), True)


if __name__ == "__main__":
    unittest.main()