import unittest

from solutions.Dif_Tw_Str import find_the_difference


class TestFindTheDifference(unittest.TestCase):
    """Unit tests for the `find_the_difference` function."""

    def test_added_character_at_end(self):
        """Test when the added letter is at the end of the string."""
        self.assertEqual(find_the_difference("abcd", "abcde"), "e")

    def test_added_character_at_start(self):
        """Test when the added letter is at the start of the string."""
        self.assertEqual(find_the_difference("bcd", "abcd"), "a")

    def test_empty_original_string(self):
        """Test when the original string is empty."""
        self.assertEqual(find_the_difference("", "y"), "y")

    def test_repeated_characters(self):
        """Test when the added letter is repeated in the string."""
        self.assertEqual(find_the_difference("aabb", "aabbc"), "c")

    def test_large_input_strings(self):
        """Test with longer strings to ensure performance."""
        s = "a" * 1000
        t = s + "z"
        self.assertEqual(find_the_difference(s, t), "z")

    def test_unicode_characters(self):
        """Test strings with non-ASCII characters."""
        self.assertEqual(find_the_difference("😊😊", "😊😊🎉"), "🎉")

    def test_special_characters(self):
        """Test strings with special characters."""
        self.assertEqual(find_the_difference("!@#", "!@#$"), "$")

    def test_added_character_in_middle(self):
        """Test when the added character is in the middle of the string."""
        self.assertEqual(find_the_difference("abde", "abcde"), "c")


if __name__ == "__main__":
    unittest.main()
