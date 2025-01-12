#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for the `find_single_number` module.

This tests the correctness of the function `find_single_number`:
    - Different numbers of elements in the input list.
    - Defensive assertions for invalid inputs.
    - Boundary cases like empty and large lists.

Author: Mudassra Taskeen
Date: 2025-01-07
"""

import unittest
from find_single_number import find_single_number




class TestFindSingleNumber(unittest.TestCase):
    """
    Unit tests for the `find_single_number` function.
    """

    def test_single_element(self):
        """
        Test the case when there is only one element in the list.
        """
        self.assertEqual(find_single_number([1]), 1)

    def test_two_elements(self):
        """
        Test the case when there are two elements in the list.
        """
        self.assertEqual(find_single_number([2, 2, 1]), 1)

    def test_multiple_elements(self):
        """
        Test the case when there are multiple elements with one unique element.
        """
        self.assertEqual(find_single_number([4, 1, 2, 1, 2]), 4)

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

    def test_boundary_large_list(self):
        """
        Test boundary case for a large list.
        """
        nums = [i for i in range(1, 1000)] * 2 + [1001]
        self.assertEqual(find_single_number(nums), 1001)


if __name__ == "__main__":
    unittest.main()
