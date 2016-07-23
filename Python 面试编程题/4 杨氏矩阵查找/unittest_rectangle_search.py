#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 对杨氏矩阵查找的几种解法进行单元测试
"""
import unittest
from rectangle_search import python_style_solve, c_style_solve

__author__ = '__L1n__w@tch'


class TestAnswer(unittest.TestCase):
    def setUp(self):
        self.repeat_list = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
        self.no_repeat_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]

    def test_normal(self):
        # 测试数字在其中的情况
        wait_to_search = [1, 9, 2, 12, 4, 13, 6, 15, 11, 8, 10, 7, 9, 4, 8, 2]
        print("二维数组: ".format(self.repeat_list))
        for each_number in wait_to_search:
            print("测试查找数字: {}".format(each_number))
            self.failUnless(python_style_solve(self.repeat_list, each_number))
            self.failUnless(
                c_style_solve(self.repeat_list, len(self.repeat_list), len(self.repeat_list[0]), each_number))

            # 测试数字不在其中的情况
            # self.failIf()


if __name__ == "__main__":
    pass
