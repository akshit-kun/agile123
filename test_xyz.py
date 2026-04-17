"""Unit tests for xyz.py"""

import unittest
from xyz import add_numbers


class TestAddNumbers(unittest.TestCase):
    """Test cases for add_numbers function."""

    def test_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_mixed_numbers(self):
        self.assertEqual(add_numbers(5, -3), 2)


if __name__ == "__main__":
    unittest.main()