#!/bin/env python2
# -*- coding: utf-8 -*-
# version: Python2.X
"""
题目描述
"""

__author__ = '__L1n__w@tch'


def solve(n):
    pass


if __name__ == "__main__":
    question = list()
    while True:
        try:
            n = raw_input()
            n = float(n)
            if n < 0:
                print("{:.6f}".format(max(question)))
                break
            else:
                question.append(n)
        except EOFError:
            break
