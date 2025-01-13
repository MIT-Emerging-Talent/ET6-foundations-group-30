import unittest
from solutions.three_sum import three_sum


class TestThreeSum(unittest.TestCase):
    """Unit tests for the three_sum function."""

    def test_basic_case(self):
        """Test basic example with valid triplets."""
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(sorted(three_sum(nums)), sorted(expected))

    def test_no_triplets(self):
        """Test when no triplets exist."""
        nums = [0, 1, 1]
        expected = []
        self.assertEqual(three_sum(nums), expected)

    def test_all_zeros(self):
        """Test all elements as zero."""
        nums = [0, 0, 0, 0]
        expected = [[0, 0, 0]]
        self.assertEqual(sorted(three_sum(nums)), sorted(expected))

    def test_repeated_numbers(self):
        """Test list with repeated numbers."""
        nums = [1, 1, 1, 1]
        expected = []
        self.assertEqual(three_sum(nums), expected)

    def test_large_input(self):
        """Test with very large input arrays."""
        nums = [1, -1, 0] * 10000
        # Expecting a valid triplet
        expected = [[-1, 0, 1]]
        self.assertEqual(sorted(three_sum(nums)), sorted(expected))

    def test_invalid_input(self):
        """Test with invalid non-integer input."""
        nums = [1, "a", None]
        with self.assertRaises(ValueError):
            three_sum(nums)


if __name__ == "__main__":
    unittest.main()
