def find_the_difference(s: str, t: str) -> str:
    """
    Finds the letter that was added to string t after shuffling string s.

    Parameters:
        s (str): Original string.
        t (str): Modified string with one extra letter.

    Returns:
        str: The letter that was added.

    Examples:
        >>> find_the_difference("abcd", "abcde")
        'e'
        >>> find_the_difference("", "y")
        'y'
    """
    result = 0
    # XOR all characters in both strings
    for char in s + t:
        result ^= ord(char)
    return chr(result)
