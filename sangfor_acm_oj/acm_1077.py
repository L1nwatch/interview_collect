#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
题目描述
编写程序，给出一个其值不超过12345678的正整数，求出它是几位数。

输入
不超过12345678的正整数.

输出
该正整数的位数

样例输入
31888
样例输出
5
"""

__author__ = '__L1n__w@tch'


def solve(number):
    return len(str(number))


if __name__ == "__main__":
    while True:
        try:
            num = int(input())
            print solve(num)
        except EOFError:
            break
