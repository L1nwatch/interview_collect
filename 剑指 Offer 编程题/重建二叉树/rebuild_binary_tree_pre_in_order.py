#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
根据前序和中序重建二叉树
"""

__author__ = '__L1n__w@tch'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


def post_order_print(list_node):
    if list_node:
        if list_node.left:
            post_order_print(list_node.left)
        if list_node.right:
            post_order_print(list_node.right)
        print(list_node.val, end=" ")


if __name__ == "__main__":
    pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
    in_order = [4, 7, 2, 1, 5, 3, 8, 6]
    root = Solution().reConstructBinaryTree(pre_order, in_order)
    post_order_print(root)
