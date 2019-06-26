#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python2.X
"""
题目描述
从键盘输入一年份，判断年份是否为闰年。

输入
输入一整数，表示年份。

输出
输出判断结果。是闰年输出"Yes"；不是闰年输出"No"。

样例输入
2011
样例输出
No
"""

__author__ = '__L1n__w@tch'


def is_leap(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


def solve(number):
    if is_leap(number):
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    while True:
        try:
            num = int(input())
            print solve(num)
        except EOFError:
            break
