"""
Tests for the 'find_single_number' module.

Author: Mudassra Taskeen
Created on: 2025-01-07
"""

import unittest
from ..find_single_number import find_single_number


class TestFindSingleNumber(unittest.TestCase):
    """Unit tests for the find_single_number function."""

    # Standard Cases
    def test_single_element(self):
        self.assertEqual(find_single_number([1]), 1)

    def test_positive_and_negative_integers(self):
        self.assertEqual(find_single_number([-1, 2, -1, 3, 2]), 3)

    def test_includes_zero(self):
        self.assertEqual(find_single_number([0, 1, 0, -2, -2]), 1)

    def test_all_negative_numbers(self):
        self.assertEqual(find_single_number([-3, -1, -3, -2, -2]), -1)

    # Edge Cases
    def test_empty_list(self):
        with self.assertRaises(AssertionError):
            find_single_number([])

    # Special Cases
    def test_single_number_with_floats(self):
        with self.assertRaises(AssertionError):
            find_single_number([1.5, 2, 2, 1.5, 3])

    def test_invalid_input(self):
        with self.assertRaises(AssertionError):
            find_single_number("not a list")

    def test_defensive_non_integer_elements(self):
        with self.assertRaises(AssertionError):
            find_single_number([1, "2", 3])

    # Performance/Boundary Cases
    def test_boundary_large_list(self):
        nums = [i for i in range(1, 1000)] * 2 + [1001]
        self.assertEqual(find_single_number(nums), 1001)


if __name__ == "__main__":
    unittest.main()
