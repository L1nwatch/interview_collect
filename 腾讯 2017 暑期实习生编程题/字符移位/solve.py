#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
# 参考资料
    http://www.cnblogs.com/duanguyuan/p/5675179.html
# 思路
    遍历 + 移动
"""
__author__ = '__L1n__w@tch'


def no_extra_space_swap(a, b):
    """
    不能构建额外空间, 那么交换移动元素使用位操作的那个版本 swap()
    原理是异或了 2 次相当于没有异或
    :param a: 'a'
    :param b: 'b'
    :return: 'b', 'a'
    """
    a, b = ord(a), ord(b)
    a ^= b
    b ^= a
    a ^= b
    return chr(a), chr(b)


def post_order_move(s):
    """
    把一个字符串的大写字母放到字符串的后面，各个字符的相对位置不变，且不能申请额外的空间。
    :param s: "AkleBiCeilD"
    :return: "kleieilABCD"
    """
    s = list(s)
    last = len(s) - 1
    for i in range(last, -1, -1):
        if s[i].islower():
            continue
        else:
            s[i], s[last] = no_extra_space_swap(s[i], s[last])
            for j in range(i, last - 1):
                s[j], s[j + 1] = no_extra_space_swap(s[j], s[j + 1])
            last -= 1

    return "".join(s)


if __name__ == "__main__":
    tests = ["AkleBiCeilD"]
    for each_test in tests:
        assert post_order_move(each_test) == "kleieilABCD"
