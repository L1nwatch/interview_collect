#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 单元测试快排
"""
import random
import unittest
from qsort import qsort


__author__ = '__L1n__w@tch'


class TestQSort(unittest.TestCase):
    def test_qsort(self):
        for i in range(30):
            list_wait_to_sort = [random.randint(-1000, 1000) for i in range(100)]
            self.failUnless(sorted(list_wait_to_sort) == qsort(list_wait_to_sort))
