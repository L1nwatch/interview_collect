#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python2.X
"""
题目描述
从键盘输入一学生某科目成绩x，判断学生成绩等级。如果x<0或x>100，输出"Error"；如果90<=x<=100，等级为'A'；如果80<=x<90，等级为'B'；如果在70<=x<80，等级为'C'；如果60<=x<70，等级为'D'；如果成绩小于60，等级为'E'。

输入
输入5行测试数据，每个测试数据代表一个成绩x，x为单精度浮点型数据。

输出
输入数据小于0或大于100，输出字符串"Error"；

输入数据在0到100之间，输出等级，等级为一字符。或为'A'；或为'B'；或为'C'；或为'D'；或为'E'。

根据输入的5行测试数据，对应输出5行结果，每个结果输出后要换行。

样例输入
99.99
100.7788
81
55
-5.7

样例输出
A
Error
B
E
Error

"""

__author__ = '__L1n__w@tch'


def solve(question):
    number = float(question)

    if 90 <= number <= 100:
        result = "A"
    elif 80 <= number < 90:
        result = "B"
    elif 70 <= number < 80:
        result = "C"
    elif 60 <= number < 70:
        result = "D"
    elif 0 <= number < 60:
        result = "E"
    else:
        result = "Error"

    return result


if __name__ == "__main__":
    while True:
        try:
            problem_input = raw_input()
            print solve(problem_input)
        except EOFError:
            break
