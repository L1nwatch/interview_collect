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

# C/C++ 版本最终提交
注意对 length 参数的理解, 还有这里返回结果是直接修改 str 而不是重新申请一段内存空间

```c++
//length为牛客系统规定字符串输出的最大长度，固定为一个常数
class Solution {
public:
    void replaceSpace(char *str, int length)
    {
        // 这其实可以忽略
        if (str == NULL || length < 0)
        {
            return;
        }

        // 遍历一遍数一下有多少个空格
        int space_numbers = 0;
        int i = 0;
        while (str[i] != '\0') // 注意不能数 length, 否则会越界
        {
            if (str[i++] == ' ')
            {
                ++space_numbers;
            }
        }

        // 计算替换后的长度
        int raw_length = strlen(str);
        int after_replace_length = raw_length + space_numbers * 2;

        // 定义指针
        int point_to_raw, point_to_new;
        point_to_new = after_replace_length;
        point_to_raw = raw_length;

        // while 循环遍历, 条件是两个索引值相等
        // while 结构体实现替换操作
        while (point_to_new != point_to_raw)
        {
            if (str[point_to_raw] != ' ')
            {
                str[point_to_new] = str[point_to_raw];
                --point_to_new;
            }
            else
            {
                str[point_to_new] = '0';
                str[point_to_new - 1] = '2';
                str[point_to_new - 2] = '%';
                point_to_new -= 3;
            }
            --point_to_raw;
        }

    }
};
```
