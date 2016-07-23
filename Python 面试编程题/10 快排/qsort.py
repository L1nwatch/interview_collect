#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 快排的 Python 实现
"""

__author__ = '__L1n__w@tch'


def qsort(a_list):
    if len(a_list) == 0:
        return a_list
    else:
        pivot = a_list[0]
        small = qsort([x for x in a_list[1:] if x < pivot])
        big = qsort([x for x in a_list[1:] if x >= pivot])
        return small + [pivot] + big


if __name__ == "__main__":
    List = [1, 3, 5, 1, 2]
    print(qsort(List))
