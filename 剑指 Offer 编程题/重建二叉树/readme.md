# 题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

# Python 最终提交
```python
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if pre and tin:
            # 找到根节点
            root = TreeNode(pre[0])

            # 计算根节点在中序中的索引
            root_position_in_order = tin.index(root.val)

            # 计算左子树长度
            left_length = root_position_in_order
            right_length = len(tin) - root_position_in_order - 1

            # 比该索引值小的为左子树
            if left_length > 0:
                root.left = Solution().reConstructBinaryTree(pre[1:root_position_in_order + 1],
                                                             tin[:root_position_in_order])

            # 计算右子树长度
            if right_length > 0:
                # 比该索引值大的为右子树
                root.right = Solution().reConstructBinaryTree(pre[root_position_in_order + 1:],
                                                              tin[root_position_in_order + 1:])

            return root
```

# C/C++ 最终提交
思路差不多, 不过换了种实现法

```c++
class Solution {
public:
    struct TreeNode *reConstructBinaryTree(vector<int> pre, vector<int> in)
    {
        if (pre.size() > 0 && in.size() > 0)
        {
            TreeNode * root = new TreeNode(pre[0]);

            vector<int>::iterator root_position_in_order = find(in.begin(), in.end(), root->val);

            int left_length = root_position_in_order - in.begin();


            root->left = Solution().reConstructBinaryTree(
                    vector<int>(pre.begin() + 1, pre.begin() + left_length + 1),
                    vector<int>(in.begin(), root_position_in_order));
            root->right = Solution().reConstructBinaryTree(
                    vector<int>(pre.begin() + left_length + 1, pre.end()),
                    vector<int>(root_position_in_order + 1, in.end()));

            return root;
        }
        return NULL;
    }
};
```