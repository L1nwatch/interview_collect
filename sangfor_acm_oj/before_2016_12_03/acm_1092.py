#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python2.X
"""
题目描述
斐波那契数列为：0、1、1、2、3、5、8、13、21、34、55、……，根据该数列总结出的规律为：

f(0)=0

f(1)=1

f(n)=f(n-1)+f(n-2)  (当n>1时）

求斐氏数列的f(n)。

假设f(n)的值所占内存不会超过4个字节。

输入
输入包括若干行，每行输入一个正整数n，若输入－1则结束。

输出
对于每行输入的n的值，对应输出f(n)，每个输出单独占一行。若输入是－1，则不输出任何结果。

样例输入
6
7
8
9
-1
样例输出
8
13
21
34
"""

__author__ = '__L1n__w@tch'


def solve(n, fib_dict):
    if dict(fib_dict).has_key(n):
        return fib_dict[n]
    else:
        max_order = len(fib_dict) - 1

        while max_order != n:
            fib_dict[max_order + 1] = fib_dict[max_order] + fib_dict[max_order - 1]
            max_order += 1

        return fib_dict[max_order]


if __name__ == "__main__":
    fib_dict = {0: 0, 1: 1}

    while True:
        try:
            n = input()
            if n == -1:
                break
            else:
                print(solve(n, fib_dict))
        except EOFError:
            break
