"""
Tests for the reverse_string function.
"""

import unittest

from solutions.reverse_string import reverse_string


class TestReverseString(unittest.TestCase):
    """
    Unit tests for the reverse_string function.
    """

    def test_reverse_simple_string(self):
        """
        Test that it correctly reverses a simple string.
        """
        s = ["h", "e", "l", "l", "o"]
        reverse_string(s)
        self.assertEqual(s, ["o", "l", "l", "e", "h"])

    def test_reverse_palindrome(self):
        """
        Test that a palindrome remains unchanged after reversal.
        """
        s = ["m", "a", "d", "a", "m"]
        reverse_string(s)
        self.assertEqual(s, ["m", "a", "d", "a", "m"])

    def test_single_character_string(self):
        """
        Test that a single-character string remains unchanged.
        """
        s = ["A"]
        reverse_string(s)
        self.assertEqual(s, ["A"])

    def test_empty_string(self):
        """
        Test that an empty list remains unchanged.
        """
        s = []
        reverse_string(s)
        self.assertEqual(s, [])

    def test_mixed_characters_string(self):
        """
        Test that it correctly reverses a string with mixed characters.
        """
        s = ["1", "2", "!", "@", "a", "b"]
        reverse_string(s)
        self.assertEqual(s, ["b", "a", "@", "!", "2", "1"])

    def test_defensive_assertion(self):
        """
        Test that the function raises an assertion error for invalid input.
        """
        with self.assertRaises(AssertionError):
            reverse_string("Not a list")


if __name__ == "__main__":
    unittest.main()
