#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
输入一个链表，从尾到头打印链表每个节点的值。

输入为链表的表头

输出为需要打印的“新链表”的表头
"""

__author__ = '__L1n__w@tch'


class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []

        if listNode:
            res.insert(0, listNode.val)  # 注意插入的是数值而不是整个对象
            while listNode.next:
                res.insert(0, listNode.next.val)
                listNode = listNode.next

        return res


if __name__ == "__main__":
    listNode = ListNode(67, ListNode(0, ListNode(24, ListNode(58, None))))
    solution = Solution()
    for each in solution.printListFromTailToHead(listNode):
        print(each)
