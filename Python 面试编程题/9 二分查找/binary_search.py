#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 考二分查找法的
"""

__author__ = '__L1n__w@tch'


def binary_search(a_list, number_to_find):
    """
    二分查找法
    :param a_list: 待查找列表
    :param number_to_find: 待查找数字
    :return: int() or False
    """
    start, end = 0, len(a_list) - 1
    while start < end:
        middle = (start + end) // 2
        if a_list[middle] > number_to_find:
            end = middle
        elif a_list[middle] < number_to_find:
            start = middle + 1
        else:
            return middle
    return start if a_list[start] == number_to_find else False


if __name__ == "__main__":
    List = [i for i in range(10)]
    print(binary_search(List, 2))
