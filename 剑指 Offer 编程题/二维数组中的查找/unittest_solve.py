#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
测试自己写的答案是否正确
"""
import random
import unittest
from python_solve import Solution

__author__ = '__L1n__w@tch'


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for i in range(33):
            array, max_number = self.create_array()
            target = array[random.randint(0, len(array) - 1)][random.randint(0, len(array[0]) - 1)]
            self.assertTrue(Solution.Find(array, target))
            self.assertFalse(Solution.Find(array, max_number + random.randint(1, max_number)))

    def create_array(self):
        """
        返回一个符合要求的二维数组以及该数组中的最大数字
        :return:
        """
        rows = random.randint(1, 33)
        columns = random.randint(1, 55)
        array = list()
        max_number = 0

        for row in range(rows):
            column_list = list()
            for column in range(columns):
                max_number += 1
                column_list.append(max_number)

            array.append(column_list)
        return array, max_number


if __name__ == "__main__":
    pass
