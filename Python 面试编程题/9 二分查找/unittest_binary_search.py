#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 单元测试二分查找
"""
import random
import unittest
from binary_search import binary_search


__author__ = '__L1n__w@tch'


class TestBinarySearch(unittest.TestCase):
    def test(self):
        list_wait_to_search = sorted([random.randint(-1000, 1000) for i in range(100)])
        number_wait_to_search = list_wait_to_search[random.randint(0, 100)]

        self.failUnless(number_wait_to_search ==
                        list_wait_to_search[binary_search(list_wait_to_search, number_wait_to_search)])
