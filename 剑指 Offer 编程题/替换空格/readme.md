# 题目描述
请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

# 思路
* Python: 直接 replace() 方法就行了....
* C/C++: 剑指 Offer 给出了两种方法, 一种是 O(n^2), 从头遍历, 遇到空格就进行替换操作, 同时把其余字符往后移动; 另一种方法是先遍历一遍, 知道有几个空格, 接着准备两个指针及一个数组, 指针分别指向原始字符串以及数组的末尾, 然后从后头开始遍历, 直至两个指针相遇

# Python 版本最终提交
感觉跟作弊一样的 Python:

```python
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(" ", "%20")
```

# C 版本最终提交
