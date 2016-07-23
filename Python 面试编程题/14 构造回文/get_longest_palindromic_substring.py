#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
参考资料:
    http://www.cnblogs.com/TenosDoIt/p/3675788.html

里面提到了 4 个算法:
    1. 暴力解法，枚举所有子串，对每个子串判断是否为回文，复杂度为O(n^3)
    2. 删除暴力解法中有很多重复的判断。很容易想到动态规划，时间复杂度O（n^2）,空间O（n^2）,动态规划方程如下：
        dp[i][j] 表示子串s[i…j]是否是回文
        初始化：dp[i][i] = true (0 <= i <= n-1);  dp[i][i-1] = true (1 <= i <= n-1); 其余的初始化为false
        dp[i][j] = (s[i] == s[j] && dp[i+1][j-1] == true)
        在动态规划中保存最长回文的长度及起点即可
    3. 以某个元素为中心，分别计算偶数长度的回文最大长度和奇数长度的回文最大长度。时间复杂度O(n^2)，空间O（1）
    4. Manacher算法，时间复杂度O(n), 空间复杂度O(n)
        查看原文链接
"""

__author__ = '__L1n__w@tch'


# 动态规划解决
def dynamic_solve(s):
    """
    动态规划解决, 方程为:
    dp[i][j] 表示子串 s[i...j] 是否是回文
    初始化:
        dp[i][i] = true (0 <= i <= n - 1) ; dp[i][i - 1] = true (1 <= i <= n - 1); 其余的初始化为 false
    方程:
        dp[i][j] = (s[i] == s[j] && dp[i+1][j-1] == true)

    :param s:
    :return:
    """
    pass


# 枚举中心法
def center_enumerate(s):
    """
    以某个元素为中心，分别计算偶数长度的回文最大长度和奇数长度的回文最大长度。时间复杂度O(n^2)，空间O（1）
    :param s: 待求的字符串
    :return: 最大长度
    """
    length = len(s)
    if length <= 1:
        return s

    start, max_length = 0, 0
    for i in range(1, length):
        # 寻找以 i-1, i 为中点偶数长度的回文
        low, high = i - 1, i
        while low >= 0 and high < length and s[low] == s[high]:
            low -= 1
            high += 1
        if high - low - 1 > max_length:
            max_length = high - low - 1
            start = low + 1

        # 寻找以 i 为中心的奇数长度的回文
        low, high = i - 1, i + 1
        while low >= 0 and high < length and s[low] == s[high]:
            low -= 1
            high += 1
        if high - low - 1 > max_length:
            max_length = high - low - 1
            start = low + 1

    return s[start:max_length]


if __name__ == "__main__":
    tests = ["abcda", "google"]
    for each_test in tests:
        print(center_enumerate(each_test))
