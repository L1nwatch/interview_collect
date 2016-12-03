#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python2.X
"""
题目描述
输入一个其值不大于32767的正整数，将各位数字分离出来，依次显示。

输入
不大于32767的正整数

输出
输出正整数的各位数字，各位数字间用逗号隔开，最后一位数字之后换行。

样例输入
32767
样例输出
3,2,7,6,7
"""

__author__ = '__L1n__w@tch'


def solve(number):
    return ",".join(list(str(number)))


if __name__ == "__main__":
    while True:
        try:
            num = int(input())
            print solve(num)
        except EOFError:
            break
