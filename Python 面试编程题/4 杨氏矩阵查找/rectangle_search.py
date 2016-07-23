#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" GitHub 上只给了题目没给源代码, 是嫌太简单了吗...

题目描述:
    在一个 m 行 n 列二维数组中, 每一行都按照从左到右递增的顺序排序, 每一列都按照从上到下递增的顺序排序.
    请完成一个函数, 输入这样的一个二维数组和一个整数, 判断数组中是否含有该整数

解答思路:
    参考: 剑指 Offer (面试题 3)
    总结查找的过程，发现规律如下：
        首先选取数组中右上角的数字。如果该数字等于要查找的数字，查找过程结束；
        如果该数字大于要查找的数字，剔除这个数字所在的列；
        如果该数字小于要查找的数字，剔除这个数字所在的行。
        也就是说如果要查找的数字不在数组的右上角，则每一次都在数组的查找范围中剔除一行或者一列，这样每一步都可以缩小查找的范围，
        直到找到要查找的数字，或者查找范围为空。
"""
import timeit
import random

__author__ = '__L1n__w@tch'


def python_style_solve(a_list, number_to_find):
    """
    用 Python 的风格解决, 思路是把二维数组转换为一维数组, 然后执行查找
    :param a_list: 要查找的二维数组
    :param number_to_find: 待查找的数字
    :return: True or False
    """
    sum_list = list()
    for each in a_list:
        sum_list.extend(each)
    if number_to_find in sum_list:
        return True
        # print("Found!")


def c_style_solve(a_list, rows, columns, number_to_find):
    """
    用 C 的风格解决, 思路参考剑指 Offer
    :param a_list: 要查找的二维数组
    :param rows: 行
    :param columns: 列
    :param number_to_find: 待查找的数字
    :return: True or False
    """
    found = False

    if a_list is not None and rows > 0 and columns > 0:
        row, column = 0, columns - 1
        while row < rows and column >= 0:
            if a_list[row][column] == number_to_find:
                found = True
                break
            elif a_list[row][column] > number_to_find:
                column -= 1
            else:
                row += 1
    return found


if __name__ == "__main__":
    python_time = list()
    c_time = list()

    for i in range(30):
        number = random.choice([i for i in range(9)])
        print("第 {} 次, 查找数字: {}".format(i + 1, number))

        test_list = [[i for i in range(3)], [i for i in range(3, 6)], [i for i in range(6, 9)]]
        time_cost = timeit.timeit("python_style_solve(test_list, {})".format(number),
                                  setup="from __main__ import python_style_solve, test_list")
        print("Python 风格执行时间: {} s".format(time_cost))
        python_time.append(time_cost)

        time_cost = timeit.timeit("c_style_solve(test_list, len(test_list), len(test_list[0]), {})".format(number),
                                  setup="from __main__ import c_style_solve, test_list")
        print("C 风格执行时间: {} s".format(time_cost))
        c_time.append(time_cost)

    print("Python 平均时间: {}, C 平均时间: {}".format(sum(python_time) / len(python_time), sum(c_time) / len(c_time)))
