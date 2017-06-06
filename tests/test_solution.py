from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        n = 4
        res = solution(n)

        self.assertEqual(res[1], 1)
        self.assertEqual(res[2], 4)
        self.assertEqual(res[3], 9)
        self.assertEqual(res[4], 16)

