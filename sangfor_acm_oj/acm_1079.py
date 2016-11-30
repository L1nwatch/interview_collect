#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
题目描述
从键盘输入一个字符，判断它是字母、数字或其它字符。

输入
从键盘输入一个字符。注意：不用提示信息。

输出
若输入的字符是字母，输出"alphabetic character"；

若输入的字符是数字，输出"digital character"；

若输入的字符是其它字符，输出"other character"；

样例输入
6
样例输出
digital character
"""
import string


__author__ = '__L1n__w@tch'


def solve(a_char):
    if a_char in string.ascii_letters:
        return "alphabetic character"
    elif a_char in string.digits:
        return "digital character"
    else:
        return "other character"

if __name__ == "__main__":
    while True:
        try:
            char = raw_input()
            print solve(char)
        except EOFError:
            break
