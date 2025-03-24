import unittest
from addition import add_numbers  # Import function from your main code file


class TestAddition(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
