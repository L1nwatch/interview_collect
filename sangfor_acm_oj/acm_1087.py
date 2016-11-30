#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python2.X
"""
题目描述
判断正整数x是否为素数。

质数又称素数。指在一个大于1的自然数中，除了1和此整数自身外，没法被其他自然数整除的数。换句话说，只有两个正因数（1和自己）的自然数即为素数。比1大但不是素数的数称为合数。1和0既非素数也非合数。

输入
先输入一个整数n（表示后面要输入n个测试数据）；

然后输入n个测试数据，每个测试数据是一个正整数x。

输出
与n个输入的正整数x相对应，输出判断结果。如果是素数，输出"Yes"，不是素数，输出"No"。

样例输入
5
7
8
795
181
888
样例输出
Yes
No
No
Yes
No
"""
# import gmpy2

__author__ = '__L1n__w@tch'


def is_prime_number(number):
    if number == 0 or number == 1:
        return False
    elif number == 2:
        return True
    for i in range(2, int(number ** 0.5 + 1)):
        if number % i == 0:
            return False

    return True


def solve(question):
    number = question

    if is_prime_number(number):
        result = "Yes"
    else:
        result = "No"

    return result


if __name__ == "__main__":
    while True:
        try:
            number_of_problems = input()
            for i in range(number_of_problems):
                problem_input = input()
                print solve(problem_input)
        except EOFError:
            break
