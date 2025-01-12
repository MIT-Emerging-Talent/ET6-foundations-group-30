"""
Module: single_number

Author: Mudassra Taskeen
Date: 2025-01-07

This module provides a function to find the single number in a list where all other numbers appear twice.
"""


def find_single_number(numbers: list[int]) -> int:
    """
    Returns the number that appears only once in the list, where all other numbers appear twice.

    Parameters:
        numbers (list[int]): A list of integers where every element appears twice except for one.

    Returns:
        int: The single number that appears only once.

    Raises:
        AssertionError: If the input list is empty or if input is not a list or contains non-integer elements.

    Assumptions:
        - The input is always a list of integers.

    Examples:
        >>> find_single_number([2, 2, 1])
        1

        >>> find_single_number([4, 1, 2, 1, 2])
        4

        >>> find_single_number([1])
        1

    Example:
        nums = [4, 1, 2, 1, 2]
        print(find_single_number(nums))
        # Output: 4

    Defensive Assertions:
        - Ensures the input is a list of integers.
    """
    # Check for valid input type
    assert isinstance(numbers, list), "Input must be a list"

    # Ensure list is not empty
    assert len(numbers) > 0, "List cannot be empty"

    # Ensure all elements are integers
    assert all(isinstance(current_number, int) for current_number in numbers), (
        "Each element must be an integer"
    )

    # Logic to find the single number
    single_number = 0

    for current_number in numbers:
        single_number ^= (
            current_number  # XOR operation, all duplicate numbers cancel out
        )

    return single_number
