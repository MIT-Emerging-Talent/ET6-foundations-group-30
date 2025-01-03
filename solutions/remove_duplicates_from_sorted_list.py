#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module: remove_duplicates_from_sorted_list
Description: This module provides a function to remove duplicates from a sorted linked list.
The function ensures each element appears only once while maintaining the sorted order.

Created on: 31 12 24
@author: Muhammad Shahroz
"""

from typing import Optional


class ListNode:
    """A node in a singly linked list."""

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def remove_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Removes duplicates from a sorted linked list.

    Parameters:
        head (Optional[ListNode]): The head node of the sorted linked list.

    Returns:
        Optional[ListNode]: The head node of the modified linked list with duplicates removed.

    Raises:
        AssertionError: If the argument is not of type ListNode or None.

    Examples:
        >>> head = ListNode(1, ListNode(1, ListNode(2)))
        >>> result = remove_duplicates(head)
        >>> result.val, result.next.val, result.next.next is None
        (1, 2, True)

        >>> head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        >>> result = remove_duplicates(head)
        >>> result.val, result.next.val, result.next.next.val
        (1, 2, 3)
    """
    assert head is None or isinstance(
        head, ListNode
    ), "Input must be a ListNode or None."

    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head
