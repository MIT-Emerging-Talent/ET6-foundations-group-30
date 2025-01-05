import unittest

from solutions.max_profit import max_profit


class MaxProfit(unittest.TestCase):
    """Tests for max_profit function"""

    def test_basic_case(self):
        """Buys at 1 and sells at 5, then buys at 3 and sells at 6, for a total profit of 7."""
        self.assertEqual(max_profit([7,1,5,3,6,4]), 7)

    def test_all_increasing_prices(self):
        """Buys at 1 and sells at 5, for a total profit of 4."""
        self.assertEqual(max_profit([1,2,3,4,5]), 4)

    def test_decreasing_prices(self):
        """Returns 0 when prices only decrease, as no profit can be made."""
        self.assertEqual(max_profit([7,6,4,3,1]), 0)

    def test_constant_prices(self):
        """Returns 0 for constant prices, as no profit can be made."""
        self.assertEqual(max_profit([5,5,5,5,5]), 0)

    def test_single_day_price(self):
        """Returns 0 for single day prices, as no profit can be made."""
        self.assertEqual(max_profit([10]), 0)

    def test_alternating_prices(self):
        """Buys at 10 and sells at 20, three times, for a total profit of 30."""
        self.assertEqual(max_profit([10,20,10,20,10,20]), 30)

    def test_float_prices(self):
        """Returns a total profit of 35.0."""
        self.assertEqual(max_profit([5.5,10.5,20.5,10.5,30.5]), 35.0)

    def test_large_price_difference(self):
        """Buys at 1 and sells at 30001 for a profit of 30000."""
        self.assertEqual(max_profit([1, 30001]), 30000)

    def test_empty_prices(self):
        """Returns 0 for an empty list of prices."""
        self.assertEqual(max_profit([]), 0)

    def test_negative_prices(self):
        """Raises an AssertionError for negative price values."""
        with self.assertRaises(AssertionError):
            max_profit([10, -5, 2, 3])

    def test_non_list_input(self):
        """Raises an AssertionError for non_list inputs."""
        with self.assertRaises(AssertionError):
            max_profit(None)

    def test_non_numeric_values(self):
        """Raises an AssertionError for non_numeric_values."""
        with self.assertRaises(AssertionError):
            max_profit([1.5, "2", 3])
