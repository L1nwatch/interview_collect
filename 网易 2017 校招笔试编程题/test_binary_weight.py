#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
这里的版本是一个超时但是正确的版本, 用这个版本来进行测试
"""
import unittest
from binary_weight import solve

__author__ = '__L1n__w@tch'


class TestBinaryWeightSolve(unittest.TestCase):
    def test_solve(self):
        for i in range(1, 1000000000):
            test_answer = solve(i)
            right_answer = TestBinaryWeightSolve.__right_answer(i)
            log_message = "i = {}, right: {}, my_answer: {}".format(i, right_answer, test_answer)
            self.assertEqual(right_answer, test_answer, log_message)

    @staticmethod
    def __right_answer(n):
        weight_n = TestBinaryWeightSolve.__get_weight(n)
        for i in range(n + 1, 1000000000):
            if TestBinaryWeightSolve.__get_weight(i) == weight_n:
                return i
        raise RuntimeError("[*] 自己的算法有问题了")

    @staticmethod
    def __get_weight(number):
        return bin(number).count("1")


if __name__ == "__main__":
    pass
