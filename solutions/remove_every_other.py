# remove_every_other.py

"""
Module: remove_every_other
Author: Mojtaba Fayyaz
Date: 2024-12-29

This module provides a utility function to remove every second element from a list.
"""


def remove_every_other(arr: list) -> list:
    """
    Removes every second element from the input list.

    Parameters:
        arr (list): A list of elements from which every second element will be removed.

    Returns:
        list: A new list containing only every other element starting with the first.

    Assumptions:
        - The input is always a non-empty list.

    Doctests:
        >>> remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep"])
        ['Keep', 'Keep', 'Keep']

        >>> remove_every_other([1, 2, 3, 4, 5])
        [1, 3, 5]

        >>> remove_every_other(["A"])
        ['A']

    Example:
        arr = ["Apple", "Banana", "Cherry"]
        print(remove_every_other(arr))
        # Output: ['Apple', 'Cherry']

    Defensive Assertions:
        - Ensures the input is a list.
    """
    assert isinstance(arr, list), "Input must be a list"
    return arr[::2]
