#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python2.X
"""
题目描述
求水仙花数。水仙花数是一个3位正整数，其值等于其各个数位的立方之和。

输入
无

输出
输出所有水仙花数，每个水仙花数单独占一行。

样例输出
153
370
371
407
"""
# import gmpy2

__author__ = '__L1n__w@tch'


def is_shuixianhua(number):
    raw_number = number
    sum_of_all = 0
    for each_number in str(number):
        sum_of_all += int(each_number) ** 3

    if raw_number == sum_of_all:
        return True
    else:
        return False


def solve():
    for i in range(100, 1000):
        if is_shuixianhua(i):
            print i


if __name__ == "__main__":
    while True:
        try:
            # problem_input = input()
            solve()
            break
        except EOFError:
            break
