# 题目描述
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# 思路解释
从右上角开始查找, 如果大于右上角的数, 说明当前列不可能存在这个数; 如果小于右上角的数, 说明当前行不可能存在这个数.

# 条件限制
时间限制：1秒

空间限制：32768K

# Python 版本最终提交
```python
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, array, target):
        # write code here
        row = len(array)
        column = len(array[0])

        if row > 0 and column > 0:
            x, y = 0, column - 1  # 从右上角第一个数字开始找

            while 0 <= x < row and 0 <= y < column:
                if array[x][y] == target:
                    return True
                elif array[x][y] > target:  # 说明当前列不会有这个数了
                    y -= 1
                elif array[x][y] < target:  # 说明当前行不会有这个数了
                    x += 1
        return False
```

# C/C++ 版本最终提交
```c++
class Solution {
public:
    bool Find(vector<vector<int> > array, int target) {
        int row = array.size();
        int column = array[0].size();

        if (row > 0 && column > 0) {
            int x, y;
            x = 0, y = column - 1;
            while (x < row && y >= 0) {
                if (array[x][y] == target) {
                    return true;
                }
                else if (array[x][y] > target) {
                    --y;
                }
                else {
                    ++x;
                }
            }
        }

        return false;
    }
};
```