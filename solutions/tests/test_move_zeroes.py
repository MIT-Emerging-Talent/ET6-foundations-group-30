#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the move_zeroes function.

Date: 2025-01-08
Author: Mudassra Taskeen
"""

import unittest
from ..move_zeroes import move_zeroes

class TestMoveZeroes(unittest.TestCase):
    """
    Unit tests for the move_zeroes function.
    Ensures that zeros are moved to the end of the list while maintaining the relative order of non-zero elements.
    """

    def test_empty_list(self):
        """
        It should handle an empty list without errors.
        """
        nums = []
        move_zeroes(nums)
        self.assertEqual(nums, [])

    def test_single_zero(self):
        """
        It should handle a list with a single zero.
        """
        nums = [0]
        move_zeroes(nums)
        self.assertEqual(nums, [0])

    def test_single_non_zero(self):
        """
        It should handle a list with a single non-zero element.
        """
        nums = [5]
        move_zeroes(nums)
        self.assertEqual(nums, [5])

    def test_no_zeroes(self):
        """
        It should handle a list with no zeros.
        """
        nums = [1, 2, 3]
        move_zeroes(nums)
        self.assertEqual(nums, [1, 2, 3])

    def test_all_zeroes(self):
        """
        It should handle a list with all zeros.
        """
        nums = [0, 0, 0]
        move_zeroes(nums)
        self.assertEqual(nums, [0, 0, 0])

    def test_mixed_elements(self):
        """
        It should correctly move zeros to the end of a mixed list.
        """
        nums = [0, 1, 0, 3, 12]
        move_zeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_zeros_at_end(self):
        """
        It should leave the list unchanged if zeros are already at the end.
        """
        nums = [1, 2, 3, 0, 0]
        move_zeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0])

    def test_large_list(self):
        """
        It should handle a large list effeciently.
        """
        nums = [0] * 1000 + [1] * 1000
        move_zeroes(nums)
        self.assertEqual(nums, [1] * 1000 + [0] * 1000)

    def test_invalid_input(self):
        """
        It should raise an assertion error for invalid input.
        """
        with self.assertRaises(AssertionError):
            move_zeroes("invalid_input")

if __name__ == "__main__":
    unittest.main()
