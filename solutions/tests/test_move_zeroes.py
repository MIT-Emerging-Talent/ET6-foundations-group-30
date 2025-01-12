"""
Unit tests for the moveZeroes function.
Test Categories:
    - Standard Cases: Various input arrays with different combinations of zeros and non-zeros
    - Edge Cases: Arrays with only zeros, only non-zeros, or an empty array
    - Defensive Cases: Invalid input handling

The tests verify that the function:
    - Correctly moves zeros to the end
    - Maintains the relative order of non-zero elements
    - Handles edge cases like empty arrays and arrays with only zeros
    - Validates input types and conditions

Date: 2025-01-07
Author: Mudassra Taskeen
"""

import unittest
from ..move_zeroes import move_zeroes


class TestMoveZeroes(unittest.TestCase):
    """Test cases for moveZeroes function."""

    def test_standard_case(self):
        """It should move all zeros to the end while maintaining order."""
        nums = [0, 1, 0, 3, 12]
        move_zeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_single_zero(self):
        """It should handle a single zero correctly."""
        nums = [0]
        move_zeroes(nums)
        self.assertEqual(nums, [0])

    def test_single_non_zero(self):
        """It should handle a single non-zero element correctly."""
        nums = [5]
        move_zeroes(nums)
        self.assertEqual(nums, [5])

    def test_all_zeros(self):
        """It should handle arrays with all zeros."""
        nums = [0, 0, 0, 0]
        move_zeroes(nums)
        self.assertEqual(nums, [0, 0, 0, 0])

    def test_all_non_zeros(self):
        """It should leave arrays with no zeros unchanged."""
        nums = [1, 2, 3, 4]
        move_zeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4])

    def test_empty_array(self):
        """It should handle an empty array."""
        nums = []
        move_zeroes(nums)
        self.assertEqual(nums, [])

    def test_edge_case_with_large_numbers(self):
        """It should handle large numbers correctly."""
        nums = [1000000, 0, 999999, 0, 1]
        move_zeroes(nums)
        self.assertEqual(nums, [1000000, 999999, 1, 0, 0])

    def test_non_list_input(self):
        """It should raise AssertionError for non-list input."""
        with self.assertRaises(AssertionError):
            move_zeroes(123)

    def test_non_integer_elements(self):
        """It should raise AssertionError for non-integer elements in the list."""
        with self.assertRaises(AssertionError):
            move_zeroes([1, "a", 0])


if __name__ == "__main__":
    unittest.main()
