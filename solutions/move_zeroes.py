"""
A module provides a function to move all zeroes in an array to the end
while maintaining the relative order of the non-zero elements.

Module contents:
    move_zeroes(nums): Rearranges the given list in-place as per the described behavior.

Author: Mudassra Taskeen
Date: 2025-01-08
"""

from typing import List


def move_zeroes(nums: List[int]) -> None:
    """
    Move all 0's to the end of the input list in-place while maintaining
    the relative sequence of non-zero elements.

    Arguments:
        nums (List[int]): The input list of integers.

    Returns:
        None: The function modifies the input list in-place.

    Raises:
        AssertionError: If nums is not a list of integers.

    Examples:
        >>> nums = [0, 1, 0, 3, 12]
        >>> move_zeroes(nums)
        >>> nums
        [1, 3, 12, 0, 0]

        >>> nums = [0]
        >>> move_zeroes(nums)
        >>> nums
        [0]from typing import list

        >>> nums = [4, 0, 5, 0, 6]
        >>> move_zeroes(nums)
        >>> print(nums)
        [4, 5, 6, 0, 0]
    """

    # Defensive assertions
    assert isinstance(nums, list), "Input must be of type List"
    assert all(isinstance(x, int) for x in nums), (
        "All elements in the list must be integers"
    )
    # Implementation: Two-pointer approach

    non_zero_index = 0

    for i, num in enumerate(nums):
        if num != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]

            non_zero_index += 1
