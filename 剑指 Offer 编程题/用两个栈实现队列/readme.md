# 题目描述
用两个栈来实现一个队列，完成队列的 Push 和 Pop 操作。队列中的元素为 int 类型。

# Python 版本最终提交
```python
class Solution:
    def __init__(self):
        self.first_stack = list()
        self.second_stack = list()

    def push(self, node):
        # write code here
        self.first_stack.append(node)

    def pop(self):
        # return xx
        if len(self.second_stack) <= 0:
            while len(self.first_stack) > 0:
                self.second_stack.append(self.first_stack.pop())
        return self.second_stack.pop()
```

# C/C++ 版本最终提交
突然发现 C/C++ 的 pop() 方法并不返回值啊...
```c++
class Solution {
public:
    void push(int node)
    {
        stack1.push(node);
    }

    int pop()
    {
        if (stack2.size() <= 0)
        {
            while (stack1.size() > 0)
            {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        int result = stack2.top();
        stack2.pop();
        return result;
    }

private:
    stack<int> stack1;
    stack<int> stack2;
};
```