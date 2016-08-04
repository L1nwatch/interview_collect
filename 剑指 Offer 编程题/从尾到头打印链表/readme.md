# 题目描述
输入一个链表，从尾到头打印链表每个节点的值。

输入描述:

    输入为链表的表头

输出描述:

    输出为需要打印的“新链表”的表头

# Python 版本提交
```python
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res = list()

        if listNode:
            res.insert(0, listNode.val) # 注意插入的是数值而不是整个对象
            while listNode.next:
                res.insert(0, listNode.next.val)
                listNode = listNode.next

        return res
```

# C/C++ 版本提交
思路跟 Python 版本一样

```c++
class Solution {
public:
    vector<int> printListFromTailToHead(struct ListNode *head)
    {
        vector<int> result;

        if (head != NULL)
        {
            result.insert(result.begin(), head->val);
            while (head->next != NULL)
            {
                result.insert(result.begin(), head->next->val);
                head = head->next;
            }
        }
        return result;
    }
};
```