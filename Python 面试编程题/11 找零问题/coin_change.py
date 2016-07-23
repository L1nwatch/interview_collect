#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 找零问题, 为啥看答案有点像背包问题...
"""

__author__ = '__L1n__w@tch'


def coin_change(values, money):
    """
    背包问题解法?
    :param values: [25, 21, 10, 5, 1]
    :param money:  63
    :return: {1:1, 2:2, 3:3, 4:4, 5:1, ..., 63:3}
    """
    coin_count = {i: 0 for i in range(money_wait_to_change + 1)}

    for cents in range(1, money + 1):
        min_coins = cents  # 从第一个开始到money的所有情况初始
        for value in values:
            if value <= cents:
                temp = coin_count[cents - value] + 1  # 这不是经典的背包?
                if temp < min_coins:
                    min_coins = temp
        coin_count[cents] = min_coins
        print('面值为：{0} 的最小硬币数目为：{1} '.format(cents, coin_count[cents]))


if __name__ == '__main__':
    pocket_monkey = [25, 21, 10, 5, 1]
    money_wait_to_change = 63
    coin_change(pocket_monkey, money_wait_to_change)
