#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 好像是考归并排序的两种实现方式, 一种递归一种循环

两种实现方式都是参考 GitHub 上的
"""
__author__ = '__L1n__w@tch'


def recursion_merge_sort(list1, list2, a_list):
    def __recursion(list_wait_to_sort_1, list_wait_to_sort_2, list_after_sort):
        if len(list_wait_to_sort_1) == 0 or len(list_wait_to_sort_2) == 0:
            list_after_sort.extend(list_wait_to_sort_1)
            list_after_sort.extend(list_wait_to_sort_2)
            return list_after_sort
        elif list_wait_to_sort_1[0] < list_wait_to_sort_2[0]:
            list_after_sort.append(list_wait_to_sort_1[0])
            del list_wait_to_sort_1[0]  # 为啥不用 list1.pop(0)...
        elif list_wait_to_sort_1[0] >= list_wait_to_sort_2[0]:
            list_after_sort.append(list_wait_to_sort_2[0])
            del list_wait_to_sort_2[0]
        return __recursion(list_wait_to_sort_1, list_wait_to_sort_2, list_after_sort)

    return __recursion(list1, list2, list())


def loop_merge_sort(list1, list2):
    after_sort = list()
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            after_sort.append(list1[0])
            del list1[0]
        else:
            after_sort.append(list2[0])
            del list2[0]
    after_sort.extend(list1)
    after_sort.extend(list2)
    return after_sort


if __name__ == "__main__":
    List1 = sorted([3, 4, 1, 2])
    List2 = sorted([2, 1, 1, 1])

    test_list = recursion_merge_sort(List1[::1], List2[::1], list())
    print(test_list)

    test_list = loop_merge_sort(List1, List2)
    print(test_list)
