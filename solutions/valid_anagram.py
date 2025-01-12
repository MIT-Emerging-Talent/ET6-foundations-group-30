"""
Module for checking if two strings are valid anagrams.

This module provides functionality to determine if two strings are anagrams
of each other (contain exactly the same characters with the same frequency).

Created on: 2025-01-11
@author: Fatima
"""


def valid_anagram(first_word: str, second_word: str) -> bool:
    """
    Returns True if two strings are anagrams, otherwise False.

    Args:
        first_word: First string to compare
            Must be a string containing any characters
        second_word: Second string to compare
            Must be a string containing any characters

    Returns:
        bool: True if strings are anagrams, False otherwise

    Raises:
        AssertionError: If either input is not a string

    Examples:
        >>> valid_anagram("listen", "silent")
        True
        >>> valid_anagram("hello", "world")
        False
        >>> valid_anagram("", "")
        True
    """

    # Ensure both inputs are strings
    assert isinstance(first_word, str), "First argument must be a string"
    assert isinstance(second_word, str), "Second argument must be a string"

    # Anagrams must be of equal length
    if len(first_word) != len(second_word):
        return False

    # Create character frequency dictionary
    char_count = {}

    # Count occurrences of each character in str1
    for char in first_word:
        char_count[char] = char_count.get(char, 0) + 1

    # Decrease character counts and check if any character is missing or overused
    for char in second_word:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]

    # If all character counts are zero, the strings are anagrams
    return len(char_count) == 0
