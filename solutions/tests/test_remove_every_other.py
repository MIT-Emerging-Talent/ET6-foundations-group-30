# tests/test_remove_every_other.py

"""
Tests for the remove_every_other function.
"""
import unittest
from solutions.remove_every_other import remove_every_other  # Updated import


class TestRemoveEveryOther(unittest.TestCase):
    """
    Unit tests for remove_every_other function.
    """

    def test_removes_every_second_element(self):
        """
        Test that it correctly removes every second element.
        """
        self.assertEqual(
            remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep"]),
            ["Keep", "Keep", "Keep"],
        )

    def test_single_element_list(self):
        """
        Test that a single-element list remains unchanged.
        """
        self.assertEqual(remove_every_other(["OnlyOne"]), ["OnlyOne"])

    def test_mixed_type_list(self):
        """
        Test that it works with mixed-type lists.
        """
        self.assertEqual(remove_every_other([1, "Two", 3, "Four", 5]), [1, 3, 5])

    def test_large_list(self):
        """
        Test with a large list.
        """
        self.assertEqual(remove_every_other(list(range(10))), [0, 2, 4, 6, 8])

    def test_defensive_assertion(self):
        """
        Test that the function raises an assertion error for invalid input.
        """
        with self.assertRaises(AssertionError):
            remove_every_other("Not a list")


if __name__ == "__main__":
    unittest.main()
