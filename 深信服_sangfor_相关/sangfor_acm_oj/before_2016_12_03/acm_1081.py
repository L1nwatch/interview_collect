#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python2.X
"""
题目描述
从键盘输入2个操作数和运算符，用switch语句实现两个数的加、减、乘、除运算。

输入
按照运算表达式的顺序输入两个操作数和运算符，如2+3或88-2或25/6或21.7*3。操作数为双精度浮点型数据，运算符为'+'或'-'或'*'或'/'。

输出
输出运算结果，结果为双精度浮点型数据。输出数据后要换行。

样例输入
21.7*7
样例输出
151.900000
"""
__author__ = '__L1n__w@tch'


def solve(question):
    result = 0
    if "*" in question:
        num1, num2 = question.split("*")
        num1, num2 = float(num1), float(num2)
        result = num1 * num2
    elif "+" in question:
        num1, num2 = question.split("+")
        num1, num2 = float(num1), float(num2)
        result = num1 + num2
    elif "-" in question:
        num1, num2 = question.split("-")
        num1, num2 = float(num1), float(num2)
        result = num1 - num2
    elif "/" in question:
        num1, num2 = question.split("/")
        num1, num2 = float(num1), float(num2)
        result = num1 / num2

    # 保证小数点后 6 位
    return "{:.6f}".format(result)


if __name__ == "__main__":
    while True:
        try:
            problem_input = raw_input()
            print solve(problem_input)
        except EOFError:
            break
