"""
This module provides a like display message based on the input list of names.

Module contents:
    Returns a string that describes how many people like a post.

Author: Madiha Malikzada
Date: 2025-01-06
"""

from typing import List


# ---- define function ----
def who_likes_it(names: List[str]) -> str:
    """
    Generate a "like display message based on the input list of names

    Args:
        names (List[str]): A list of names representing people who liked a an item (post)

    Returns:
        str: A display message that describes how many people liked the post

    Raises:
        - AssertionError: If any name in the list is not a string
        - The list itself is not of type `List`

    Examples:
        >>> who_likes_it([])
        'no one likes this'
        >>> who_likes_it(["Evan"])
        'Evan likes this'
        >>> who_likes_it(["Evan", "Madiha"])
        'Evan and Madiha like this'
        >>> who_likes_it(["Evan", "Madiha", "Megan"])
        'Evan, Madiha and Megan like this'
        >>> who_likes_it(["Evan", "Madiha", "Megan", "Camila"])
        'Evan, Madiha and 2 others like this'
    """

    # Defensive assertions
    assert isinstance(names, List), "Input names should be of type List"
    assert all(isinstance(name, str) for name in names), (
        "All names should be of type string"
    )

    names_length = len(names)

    # If the list is empty, return 'no one likes this'.
    if names_length == 0:
        return "no one likes this"

    # If the list has 1-3 names, format them directly in the message.
    elif names_length == 1:
        return f"{names[0]} likes this"

    elif names_length == 2:
        return f"{names[0]} and {names[1]} like this"

    elif names_length == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"

    # For 4 or more names, summarize additional names as 'X others'.
    else:
        return f"{names[0]}, {names[1]} and {names_length - 2} others like this"
