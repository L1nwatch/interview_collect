#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 给定一个数组, 构建二叉树, 并且按层次打印这个二叉树, 以及进行深度遍历
"""
import queue
from functools import wraps

__author__ = '__L1n__w@tch'


def decorator_with_argument(sentence):
    """
    带有一个参数的修饰器
    :param sentence: 要打印的句子
    :return: 修饰器
    """

    def decorator(function):
        @wraps(function)
        def wrap(*args):
            print(sentence)
            result = function(*args)
            print("")
            return result  # 注意需要返回结果的

        return wrap

    return decorator


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


@decorator_with_argument("第一种层次遍历")
def layer_search(root):
    """
    层次遍历
    :param root: 根节点
    :return: None
    """
    stack = [root]
    while stack:
        current = stack.pop(0)
        print(current.data, end=" ")
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)


@decorator_with_argument("第二种层次遍历")
def layer_order_traverse(root):
    """
    层次遍历第二种写法, 其实就换了个数据结构
    :param root: 根节点
    :return: None
    """
    a_queue = queue.Queue()
    a_queue.put(root)
    while not a_queue.empty():
        node = a_queue.get()
        print(node.data, end=" ")
        if node.left:
            a_queue.put(node.left)
        if node.right:
            a_queue.put(node.right)


@decorator_with_argument("先序遍历")
def pre_order_traverse(root):
    """
    深度遍历, 先序遍历?
    PS: 之所以把递归封装起来是为了不重复调用装饰器
    :param root: 根节点
    :return: None
    """

    def __recursion(node):
        if not node:
            return None
        print(node.data, end=" ")
        __recursion(node.left)
        __recursion(node.right)

    return __recursion(root)


@decorator_with_argument("中序遍历")
def in_order_traverse(root):
    """
    中序遍历
    :param root: 根节点
    :return: None
    """

    def __recursion(node):
        if not node:
            return None
        if node.left:
            __recursion(node.left)
        print(node.data, end=" ")
        if node.right:
            __recursion(node.right)

    return __recursion(root)


@decorator_with_argument("后序遍历")
def post_order_traverse(root):
    """
    后序遍历
    :param root: 根节点
    :return: None
    """

    def __recursion(node):
        if not node:
            return None
        if node.left:
            __recursion(node.left)
        if node.right:
            __recursion(node.right)
        print(node.data, end=" ")

    return __recursion(root)


@decorator_with_argument("求最大树深")
def max_depth(root):
    """
    求树的最大深度
    :param root: 根节点
    :return: int()
    """

    def __recursion(node):
        if not node:
            return 0
        return max(__recursion(node.left), __recursion(node.right)) + 1

    return __recursion(root)


@decorator_with_argument("判断两棵树是否相同")
def is_same_tree(root1, root2):
    """
    递归判断两颗树是否相同
    :param root1: 根节点 1
    :param root2: 根节点 2
    :return: True or False
    """

    def __recursion(node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 and node2:
            return node1.data == node2.data \
                   and __recursion(node1.left, node2.left) \
                   and __recursion(node1.right, node2.right)
        else:
            return False

    return __recursion(root1, root2)


@decorator_with_argument("先序中序创建二叉树")
def create_binary_tree_by_pre_in_order(pre_order_list, in_order_list):
    """
    根据先序中序创建二叉树
    :param pre_order_list: [1, 3, 7, 0, 6, 2, 5, 4]
    :param in_order_list: [0, 7, 3, 6, 1, 5, 2, 4]
    :return: Node() or None
    """

    def __recursion(pre_order, in_order):
        if not pre_order:
            return None
        current = Node(pre_order[0])
        index = in_order.index(pre_order[0])
        current.left = __recursion(pre_order[1:index + 1], in_order[:index])
        current.right = __recursion(pre_order[index + 1:], in_order[index + 1:])
        return current

    return __recursion(pre_order_list, in_order_list)


@decorator_with_argument("中序后序创建二叉树")
def create_binary_tree_by_post_in_order(post_order_list, in_order_list):
    """
    根据中序后序来创建二叉树
    :param post_order_list: [0, 7, 6, 3, 5, 4, 2, 1]
    :param in_order_list: [0, 7, 3, 6, 1, 5, 2, 4]
    :return: Node() or None
    """

    def __recursion(post_order, in_order):
        if not post_order:
            return None
        current = Node(post_order[-1])
        index = in_order.index(post_order[-1])
        current.left = __recursion(post_order[:index], in_order[:index])
        current.right = __recursion(post_order[index:-1], in_order[index + 1:])

        return current

    return __recursion(post_order_list, in_order_list)


if __name__ == "__main__":
    tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
    layer_search(tree)
    layer_order_traverse(tree)
    pre_order_traverse(tree)
    in_order_traverse(tree)
    post_order_traverse(tree)
    print(max_depth(tree))

    tree2 = Node(11, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
    print(is_same_tree(tree, tree2))

    pre_order_visit = [1, 3, 7, 0, 6, 2, 5, 4]
    in_order_visit = [0, 7, 3, 6, 1, 5, 2, 4]
    tree = create_binary_tree_by_pre_in_order(pre_order_visit, in_order_visit)
    post_order_traverse(tree)

    post_order_visit = [0, 7, 6, 3, 5, 4, 2, 1]
    tree = create_binary_tree_by_post_in_order(post_order_visit, in_order_visit)
    pre_order_traverse(tree)
