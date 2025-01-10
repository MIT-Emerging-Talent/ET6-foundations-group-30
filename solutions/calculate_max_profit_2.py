#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module to calculate the maximum profit from stock trading.

Module Contents:

    - calculate_max_profit(prices: list) -> int:
    Computes the maximum profit that can be made by completing as many transactions as possible
    (buy one and sell one share of stock multiple times).

Created on: 2025-01-05
Author: Jola-Moses
"""


def calculate_max_profit(prices: list) -> int:
    """
    Returns the maximum profit from as many stock transactions as possible.

    Parameters:
        prices (list): A list of non-negative integers or floats representing the stock prices
                        on different days. Each price is greater than or equal to zero."

    Returns:
        int, float: The maximum profit that can be made from as many transactions as possible.

    Raises:
        AssertionError: If `prices` is not a list.
        AssertionError: If any element in `prices` is not a numeric type (either int or float).
        AssertionError: If any price in `prices` is less than zero.

    Examples:
        >>> calculate_max_profit([7, 1, 5, 3, 6, 4])
        7
        >>> calculate_max_profit([1, 2, 3, 4, 5])
        4
        >>> calculate_max_profit([7, 6, 4, 3, 1])
        0
    """

    assert isinstance(prices, list), "Input should be a list."
    assert all(
        isinstance(price, (int, float)) for price in prices
    ), "Prices should be integers or floats."
    assert all(
        price >= 0 for price in prices
    ), "Prices should be non-negative integers or floats."

    maximum_profit = 0

    # Compare each day's price with the previous day's, starting from the second day
    for i in range(1, len(prices)):
        # Add profit if today's price is higher than yesterday's.
        if prices[i] > prices[i - 1]:
            maximum_profit += prices[i] - prices[i - 1]

    return maximum_profit
