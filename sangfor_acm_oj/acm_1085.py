#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python2.X
"""
输入
先输入一个整数n，表示后面总共要输入n组测试数据；

然后输入n组测试数据，每组测试数据是一个双精度浮点数x。

输出
根据输入的n组测试数据，对应输出n个输出结果，每个输出结果单独占一行，即每个输出结果后要加换行符。

样例输入
3
25
-2
49
样例输出
y=125.000000
y=1.000000
y=6.000000
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
            number_of_problems = input()
            for each in range(number_of_problems):
                problem_input = raw_input()
                print solve(problem_input)
        except EOFError:
            break
