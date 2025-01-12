#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for the 'find_single_number' module.

Test Categories:
    - Standard Cases: Regular lists with varying numbers of elements.
    - Edge Cases: Boundary conditions like empty lists and lists with mixed types.
    - Special Cases: Lists with floating-point numbers and special characters.
    - Defensive Cases: Ensuring proper handling of invalid inputs.

Author: Mudassra Taskeen
Created on: 2025-01-07
"""

import unittest
from find_single_number import find_single_number


class TestFindSingleNumber(unittest.TestCase):
    """
    Unit tests for the `find_single_number` function.
    """

    # Standard Cases
    def test_single_element(self):
        """
        Test the case when there is only one element in the list.
        """
        self.assertEqual(find_single_number([1]), 1)

    def test_positive_and_negative_integers(self):
        """
        It should correctly identify the single number with both positive and negative integers.
        """
        self.assertEqual(find_single_number([-1, 2, -1, 3, 2]), 3)

    def test_includes_zero(self):
        """
        It should correctly identify the single number in a list that includes zero.
        """
        self.assertEqual(find_single_number([0, 1, 0, -2, -2]), 1)

    def test_all_negative_numbers(self):
        """
        It should correctly identify the single number when all elements are negative.
        """
        self.assertEqual(find_single_number([-3, -1, -3, -2, -2]), -1)

    # Edge Cases
    def test_empty_list(self):
        """It should raise an error or handle the case gracefully if the input list is empty."""
        with self.assertRaises(ValueError):
            find_single_number([])


def test_single_number_with_floats(self):
    """
    It should raise an error for lists containing floating-point numbers.
    """
    with self.assertRaises(TypeError):
        find_single_number([1.5, 2, 2, 1.5, 3])

    # Special Cases
    def test_invalid_input(self):
        """
        Test the case when input is not a list type.
        """
        with self.assertRaises(AssertionError):
            find_single_number("not a list")

    def test_defensive_non_integer_elements(self):
        """
        Test the case when input list contains non-integer elements.
        """
        with self.assertRaises(AssertionError):
            find_single_number([1, "2", 3])

    # Performance/Boundary Cases
    def test_boundary_large_list(self):
        """
        Test boundary case for a large list.
        """
        nums = [i for i in range(1, 1000)] * 2 + [1001]
        self.assertEqual(find_single_number(nums), 1001)


if __name__ == "__main__":
    unittest.main()
