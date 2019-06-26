#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python2.X
"""
题目描述
从键盘输入一个整数n(98000<=n<=100000),统计1至n范围内，个位数是7的素数的个数。

质数又称素数。指在一个大于1的自然数中，除了1和此整数自身外，没法被其他自然数整除的数。换句话说，只有两个正因数（1和自己）的自然数即为素数。比1大但不是素数的数称为合数。1和0既非素数也非合数。

输入
输入一个整数n(98000<=n<=100000)

输出
个位数为7的素数的个数

样例输入
100000
样例输出
2411
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
    counts = 0

    for i in range(1, number + 1):
        if str(i)[-1] == "7" and is_prime_number(i):
            counts += 1

    return counts


if __name__ == "__main__":
    while True:
        try:
            problem_input = input()
            print solve(problem_input)
        except EOFError:
            break
