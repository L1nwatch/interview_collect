#!/bin/env python2
# -*- coding: utf-8 -*-
# version: Python2.X
"""
题目描述
从键盘输入若干学生的成绩，输出其中的最高成绩。

输入
输入若干学生的成绩，输入负数时结束输入。

输出
输出最高成绩。

样例输入
8
34
345
353.88
23
-2
样例输出
353.880000
"""

__author__ = '__L1n__w@tch'


def solve(n):
    pass


if __name__ == "__main__":
    question = list()
    while True:
        try:
            n = raw_input()
            n = float(n)
            if n < 0:
                print("{:.6f}".format(max(question)))
                break
            else:
                question.append(n)
        except EOFError:
            break
