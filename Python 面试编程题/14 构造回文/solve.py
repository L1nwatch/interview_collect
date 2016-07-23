#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
# 题目描述
给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？输出需要删除的字符个数。

# 参考资料
    http://www.voidcn.com/blog/Do_Know/article/p-5978576.html

# 分析
对于这题来说，插入字符和删除字符使其成为回文串，答案是一样的.

首先求s的反串rs，然后对s和rs求最长公共子序列，要删除的字符个数就是 LCS.
"""

__author__ = '__L1n__w@tch'

MAX_LENGTH = 1010  # 1 <= s <= 1000


# 答案用动态规划解决的
def dynamic_solve(s):
    """
    动态规划求取构造回文要删除的字符个数
        dp[i][j] 表示 s1 的前 i 个字符串, s2 的后 j 个字符串中的最大公共字串

    动态方程:
        dp[i + 1][j + 1] = dp[i][j] + 1 if s1[i] == s2[j] else max(dp[i][j + 1], dp[i + 1][j])
    :param s: 原始字符串
    :return: 需要删除的字符个数
    """
    # 先求反串
    length = len(s)
    reversed_s = s[::-1]

    # 求最长公共子序列
    dp = [[0 for i in range(MAX_LENGTH)] for i in range(MAX_LENGTH)]  # 初始化

    for i in range(length):
        for j in range(length):
            if s[i] == reversed_s[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    return length - dp[length][length]  # 长度减去最长公共子序列即为所求


if __name__ == "__main__":
    tests = ["", "a", "ab", "abcda", "google",
             "zgtklhfzomzjckwmluvivvcmhjrwkuvcjrxojobpdedpamdshcwwsetfbacvonecrdvugeibglvhxuymjvoryqjwullvzglqazxrdmczyvbgakjagttrezmvrlptiwoqkrtxuroeqmryzsgokopxxdpbejmtwvpnaqrgqladdszhdwxfckmewhdvihgvacueqhvwvjxoitlpfrckxkuksaqzjpwgoldyhugsacflcdqhifldoaphgdbhaciixouavqxwlghadmfortqacbffqzocinvuqpjthgekunjsstukeiffjipzzabkuiueqnjgkuiojwbjzfynafnlcaryygqjfixaoeowhkxkbsnpsvnbxuywfxbnuoemxynbtgkqtjvzqikbafjnpbeirxxrohhnjqrbqqzercqcrcswojyylunuevtdhamlkzqnjrzibwckbkiygysuaxpjrgjmurrohkhvjpmwmmtpcszpihcntyivrjplhyrqftghglkvqeidyhtmrlcljngeyaefxnywpfsualufjwnffyqnpitgkkyrbwccqggycrvoocbwsdbftkigrkcbojuwwctknzzmvhbhbfzrqwzllulbabztqnznkqdyoqnrxhwavqhzyzvmmmphzxbikpharseywpfsqyybkynwbdrgfsaxduxojcdqcjuaywzbvdjgjqtoffasiuhvxcaockebkuxpiomqmtvsqhnyxfjceqevqvnapbk"]
    for each_test in tests:
        print(dynamic_solve(each_test))
