#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
题目描述
给出两个整数A,B

求A+B的结果

输入
A，B两个整数

0≤A, B≤1018

输出
一个整数C
样例输入
1 1
样例输出
2
"""

__author__ = '__L1n__w@tch'

if __name__ == "__main__":
    a = []
    for x in raw_input().split():
        a.append(int(x))

    print sum(a)
