#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
20160924 发现原来只是 index == len(reverse_temp) - 1: 那里写错了, 改过来之后能够通过测试了
20160924 这是之前只能通过 50% 例子的版本, 现在利用测试找出算法缺陷
"""

__author__ = '__L1n__w@tch'


def get_weight(number):
    return bin(number).count("1")


def get_start_number(number):
    temp = bin(number)[2:]
    reverse_temp = temp[::-1]
    flag = False
    for index in range(len(reverse_temp)):
        # 查找到 0
        if reverse_temp[index] == "0" and flag == False:
            continue
        # 找到所要找的数字了
        if reverse_temp[index] == "1":
            flag = True
        # 找到最后一个数字了
        if index == len(reverse_temp) - 1:
            result = "1" + "0" * (index + 1)
            return int(result, 2)
        if reverse_temp[index] == "0" and flag == True:
            result = "0" * index + "1" + reverse_temp[index + 1:]
            result = result[::-1]
            return int(result, 2)


def solve(number):
    start_number = get_start_number(number)
    weight_n = get_weight(number)
    for i in range(start_number, 1000000000):
        if get_weight(i) == weight_n:
            return i


if __name__ == "__main__":
    solve(1)
