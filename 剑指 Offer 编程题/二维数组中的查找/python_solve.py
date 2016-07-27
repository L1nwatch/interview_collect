#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
Python 解决二维数组中的查找问题
"""

__author__ = '__L1n__w@tch'


class Solution:
    # array 二维列表
    @classmethod
    def Find(cls, array, target):
        # write code here
        row = len(array)
        column = len(array[0])

        if row > 0 and column > 0:
            x, y = 0, column - 1  # 从右上角第一个数字开始找

            while 0 <= x < row and 0 <= y < column:
                if array[x][y] == target:
                    return True
                elif array[x][y] > target:  # 说明当前列不会有这个数了
                    y -= 1
                elif array[x][y] < target:  # 说明当前行不会有这个数了
                    x += 1
        return False


if __name__ == "__main__":
    solution = Solution()
    array = [[]]
    print(solution.Find(array, 9))
