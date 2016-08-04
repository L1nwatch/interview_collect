#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
利用两个栈来实现队列
"""
import queue

__author__ = '__L1n__w@tch'


class Solution:
    def __init__(self):
        self.first_stack = list()
        self.second_stack = list()

    def push(self, node):
        # write code here
        self.first_stack.append(node)

    def pop(self):
        # return xx
        if len(self.second_stack) <= 0:
            while len(self.first_stack) > 0:
                self.second_stack.append(self.first_stack.pop())
        return self.second_stack.pop()


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    q = queue.Queue()
    s = Solution()

    for each in data:
        q.put(each)
        s.push(each)

    for i in range(len(data)):
        print(s.pop(), end=" ")

    print("")

    for i in range(len(data)):
        print(q.get(), end=" ")
