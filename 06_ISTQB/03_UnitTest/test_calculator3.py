import unittest
from calculator import add, subtract, multiply, divide

# Using setUp, Context Manager Subtest
# Wie viel TCs werden ausgeführt?


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        # before each test case
        self.positive_a = 10
        self.positive_b = 5
        self.negative_a = -10
        self.negative_b = -5
        self.zero = 0

    def test_add(self):

        test_case = [
            (3, 5, 8),
            (30, 50, 80),
            (-3, -5, -8)
        ]

        for a, b, expected in test_case:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(add(a, b), expected)

    def test_invalid_types(self):

        invalid_test_cases = [
            ("a", 1),
            (1, "b"),
            ("a", "b"),
            (1, None),
            (None, 1),
        ]

        for a, b in invalid_test_cases:
            with self.subTest(a=a, b=b):
                with self.assertRaises(TypeError):
                    add(a, b)


if __name__ == "__main__":
    unittest.main()
