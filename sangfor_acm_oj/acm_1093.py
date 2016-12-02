#!/bin/env python2
# -*- coding: utf-8 -*-
# version: Python2.X
"""
题目描述
求1－n中回文数的个数。回文数指正读和反读相同的整数，即该数和它的逆序数相等。如535，282等。

输入
输入包括多行，每行输入一个正整数n（n>=1)。若输入的正整数是0，则结束输入。

输出
与输入相对应，各行对应输出1－n中，回文数的个数。

样例输入
9
44
55
0
样例输出
9
13
14
"""

__author__ = '__L1n__w@tch'


def is_huiwen(n):
    # 以下效率低一些
    # str_n = str(n)
    # return str_n == str_n[::-1]
    n = str(n)
    for i in range(len(n) / 2):
        if n[i] != n[len(n) - i - 1]:
            return False
    return True


def solve(n):
    counts = 0
    for i in range(1, n + 1):
        if is_huiwen(i):
            counts += 1
    return counts


if __name__ == "__main__":
    while True:
        try:
            n = input()
            if n == 0:
                break
            else:
                print(solve(n))
        except EOFError:
            break
