#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python2.X
"""
输入
从键盘输入一个整数n，然后按上面的公式求和。

输出
输出求和的结果s。s为双精度浮点数，精确到小数点后面8位。

样例输入
22
样例输出
0.67093591
"""

__author__ = '__L1n__w@tch'


def solve(question):
    number = question
    result = 0

    for i in range(number):
        current_num = i + 1
        result += (-1) ** (current_num + 1) * (1.0 / current_num)

    return "{:.8f}".format(result)


if __name__ == "__main__":
    while True:
        try:
            problem_input = input()
            print solve(problem_input)
        except EOFError:
            break
