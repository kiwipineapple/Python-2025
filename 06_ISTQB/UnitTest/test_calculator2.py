import unittest
from calculator import add, subtract, multiply, divide

# Using setUp, Context Manager Subtest
# Wie viel TCs werden ausgeführt?


class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # before the whole tests
        print("setUpClass Method is runned once")
        cls.dbconn = "MyConn"

    @classmethod
    def tearDownClass(cls):
        # after the whole tests
        print("tearDownClass Method is runned once")
        cls.db = None

    def setUp(self) -> None:
        # before each test case
        self.positive_a = 10
        self.positive_b = 5
        self.negative_a = -10
        self.negative_b = -5
        self.zero = 0

    def tearDown(self):
        # after each test case
        # Clean Up Method for files, DB, Logs,...etc
        pass

    def test_add(self):

        test_case = [
            (3, 5, 8),
            (30, 50, 80),
            (-3, -5, -8)
        ]

        for a, b, expected in test_case:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(add(a, b), expected)

    def test_add_2(self):
        # using the setUp Method Instance based attributes
        test_cases = [
            (self.positive_a, self.positive_b, 15),
            (self.negative_a, self.negative_b, -15),
            (self.positive_a, self.zero, 10),
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expcted=expected):
                self.assertEqual(add(a, b), expected)

    def test_db_conn(self):
        self.assertEqual(self.dbconn, "MyConn")


if __name__ == "__main__":
    unittest.main()
