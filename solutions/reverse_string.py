"""
Module: reverse_string
Author: Mojtaba Fayyaz
Date: 2024-01-02

This module provides a utility function to reverse an array of characters in-place.
"""


def reverse_string(s: list) -> None:
    """
    Reverses the input array of characters in-place.

    Parameters:
        s (list): A list of characters to be reversed.

    Returns:
        None: The input list is modified in-place.

    Assumptions:
        - The input is always a list of characters.

    Doctests:
        >>> s = ['h', 'e', 'l', 'l', 'o']
        >>> reverse_string(s)
        >>> s
        ['o', 'l', 'l', 'e', 'h']

        >>> s = ['H', 'a', 'n', 'n', 'a', 'h']
        >>> reverse_string(s)
        >>> s
        ['h', 'a', 'n', 'n', 'a', 'H']

        >>> s = ['A']
        >>> reverse_string(s)
        >>> s
        ['A']

    Example:
        s = ['c', 'a', 't']
        reverse_string(s)
        print(s)
        # Output: ['t', 'a', 'c']

    Defensive Assertions:
        - Ensures the input is a list.
    """
    assert isinstance(s, list), "Input must be a list"
    left, right = 0, len(s) - 1

    while left < right:
        # Swap the characters at the left and right indices
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
