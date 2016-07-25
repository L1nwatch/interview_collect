#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
自己写的只能通过 10%, 只好写个单元测试来测试自己哪里错了
"""
import unittest
import random
from solve import solve

__author__ = '__L1n__w@tch'


class TestMine(unittest.TestCase):
    def test_my_answer(self):
        for i in range(233):
            length = random.randint(1, 10 ** 3)
            a_list = str()
            for j in range(length):
                a_list += "{} ".format(random.randint(0, 10 ** 4))

            right_answer = "{} {}".format(*right(length, a_list))
            my_answer = solve(length, a_list)
            self.assertEqual(right_answer, my_answer)


def right(n, a):
    try:
        n = n
        a = list(map(int, a.split()))
        # n = input()
        # a = map(int, input().split())
    except:
        exit()
    if n == 1:
        return 0, 0
    else:
        a = sorted(a)
        m = a[1] - a[0]
        for i in range(2, n):
            m = min(m, a[i] - a[i - 1])
            if m == 0:
                break
        cnt = 0
        if m == 0:
            from itertools import groupby
            for k, v in groupby(a):
                l = len(list(v))
                cnt += (l - 1) * l // 2
        else:
            for i in range(1, n):
                if a[i] - a[i - 1] == m:
                    cnt += 1
        return cnt, n * (n - 1) // 2 if a[0] == a[-1] else a.count(a[0]) * a.count(a[-1])


if __name__ == "__main__":
    unittest.main()
