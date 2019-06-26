#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python2.X
"""
输入
输入一双精度浮点数x

输出
根据分段函数，输出x对应的y值。

样例输入
25
样例输出
y=125.000000
"""
import math

__author__ = '__L1n__w@tch'


def solve(question):
    number = float(question)

    if number < 0:
        result = abs(number) / 2
    elif 0 <= number < 10:
        result = 3 + math.exp(number)
    elif 10 <= number < 20:
        result = math.log10(number)
    elif 20 <= number < 30:
        result = number ** 1.5
    elif 30 <= number < 50:
        result = number ** 0.5 - 1
    elif number >= 50:
        result = math.cos(number) * 3

    return "y={:.6f}".format(result)


if __name__ == "__main__":
    while True:
        try:
            problem_input = raw_input()
            print solve(problem_input)
        except EOFError:
            break
