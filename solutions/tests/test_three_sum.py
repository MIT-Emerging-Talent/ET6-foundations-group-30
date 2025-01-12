import unittest

from solutions.three_sum import three_sum


class TestThreeSum(unittest.TestCase):
    """Test cases for the three_sum function."""

    def test_example_case(self):
        """It should find all unique triplets that sum to zero."""
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(sorted(three_sum(nums)), sorted(expected))

    def test_no_triplets(self):
        """It should return an empty list when no triplets exist."""
        nums = [0, 1, 1]
        expected = []
        self.assertEqual(three_sum(nums), expected)

    def test_all_zeros(self):
        """It should handle cases with all elements being zero."""
        nums = [0, 0, 0]
        expected = [[0, 0, 0]]
        self.assertEqual(three_sum(nums), expected)

    def test_empty_list(self):
        """It should return an empty list for an empty input list."""
        nums = []
        expected = []
        self.assertEqual(three_sum(nums), expected)

    def test_fewer_than_three_elements(self):
        """It should return an empty list if fewer than three elements are provided."""
        nums = [1, -1]
        expected = []
        self.assertEqual(three_sum(nums), expected)

    def test_duplicates_in_triplets(self):
        """It should avoid duplicate triplets in the result."""
        nums = [-2, 0, 0, 2, 2]
        expected = [[-2, 0, 2]]
        self.assertEqual(sorted(three_sum(nums)), sorted(expected))

    def test_large_negative_and_positive_numbers(self):
        """It should handle large positive and negative numbers."""
        nums = [-(10**6), 0, 10**6, -1, 1]
        expected = [[-(10**6), 0, 10**6], [-1, 0, 1]]
        self.assertEqual(sorted(three_sum(nums)), sorted(expected))


if __name__ == "__main__":
    unittest.main()
