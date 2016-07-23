#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 对单链表实现逆置操作, 即 1 -> 2 -> 3 变为 3 -> 2 -> 1
"""

__author__ = '__L1n__w@tch'


class ListNode:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


def print_single_list(head_node):
    """
    打印单链表
    :param head_node: ListNode()
    :return: None
    """
    if head_node:
        print(head_node.data, end=" -> ")
        next_node = head_node.next_node
        while next_node:
            print(next_node.data, end=" -> ")
            next_node = next_node.next_node
        print("None")


def reverse_single_list(head_node):
    """
    GitHub 上的思路是用 3 个指针, 自己的思路是用栈来解决, 看起来 GitHub 思路简单些
    :param head_node: ListNode()
    :return: None
    """
    pre = head_node
    current = head_node.next_node
    pre.next_node = None

    while current:
        temp = current.next_node
        current.next_node = pre
        pre = current
        current = temp
    return pre


if __name__ == "__main__":
    single_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
    print_single_list(single_list)

    reversed_single_list = reverse_single_list(single_list)
    print_single_list(reversed_single_list)
