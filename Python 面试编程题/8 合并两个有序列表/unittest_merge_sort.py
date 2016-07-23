#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 测试归并排序是否正确
"""
import random
import unittest
from merge_sort import recursion_merge_sort, loop_merge_sort


__author__ = '__L1n__w@tch'


class TestMergeSort(unittest.TestCase):
    def test(self):
        for i in range(5):
            wait_to_sort = sorted([random.randint(-1000, 1000) for i in range(100)])
            wait_to_sort_2 = sorted([random.randint(-1000, 1000) for i in range(100)])

            after_sort = sorted(wait_to_sort + wait_to_sort_2)

            self.failUnless(after_sort == recursion_merge_sort(wait_to_sort[::1], wait_to_sort_2[::1], list()))
            self.failUnless(after_sort == loop_merge_sort(wait_to_sort[::1], wait_to_sort_2[::1]))


if __name__ == "__main__":
    pass
