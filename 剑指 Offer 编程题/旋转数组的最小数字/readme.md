# 题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。

例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。

NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

# Python 版本最终提交
看别人的 C/C++ 答案那么长, 结果 Python 就一行, 果然还是得自己用 C 重写

```python
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        return min(rotateArray)
```

# C/C++ 版本最终提交
根据二分查找改编的, 思路是参考剑指 Offer 里给的

```
class Solution {
public:
    int minNumberInRotateArray(vector<int> rotateArray)
    {
        if (rotateArray.size() > 0)
        {
            int low, high, middle;
            low = 0;
            high = rotateArray.size() - 1;
            middle = low;

            // 结束条件
            while (rotateArray[low] >= rotateArray[high])
            {
                // 结束条件
                if (high - low == 1)
                {
                    middle = high;
                    break;
                }

                // 求取中间的索引值
                middle = (low + high) / 2;

                // 判断中间值的大小, 知道它是前面的递增序列还是后面的递增序列
                if (rotateArray[middle] <= rotateArray[high])
                {
                    high = middle;
                }
                else if (rotateArray[middle] >= rotateArray[low])
                {
                    low = middle;
                }
            }

            return rotateArray[middle];
        }
        return 0;
    }
};
```