# 说明
题目来自于牛客网, 腾讯面试的编程题

# 原题描述
给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？

输出需要删除的字符个数。

输入描述:

输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.



输出描述:

对于每组数据，输出一个整数，代表最少需要删除的字符个数。

输入例子:

abcda

google

输出例子:

2

2

# 最终提交
```Python
# 这个思路是对的, 但是超时了
import sys

MAX_LENGTH = 1000  # 1 <= s <= 1000


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
    length = len(s)
    reversed_s = s[::-1]

    # 求最长公共子序列
    for i in range(length):
        for j in range(length):
            if s[i] == reversed_s[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    return length - dp[length][length]  # 长度减去最长公共子序列即为所求

dp = [[0 for i in range(MAX_LENGTH)] for i in range(MAX_LENGTH)]  # 初始化

for line in sys.stdin:
    print dynamic_solve(line.strip())
```