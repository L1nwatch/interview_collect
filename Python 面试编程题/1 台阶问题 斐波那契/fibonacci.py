#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 又见斐波那契数列

这回是练习了经典的面试题:
    一只青蛙一次可以跳上 1 级台阶, 也可以跳上 2 级. 求该青蛙跳上一个 n 级的台阶总共有多少种跳法?

斐波那契除了 GitHub 面试题给的那三种外, 还有我之前实现过的一种, 都整理在这个文件了
"""
import timeit
from functools import wraps

__author__ = '__L1n__w@tch'


def recursion(n):
    """
    普通的递归求斐波那契
    :param n:
    :return:
    """
    if n <= 2:
        return n
    else:
        return recursion(n - 1) + recursion(n - 2)


def memory(function):
    """
    作为修饰器存在的
    :param function:
    :return:
    """
    cache = {}

    @wraps(function)  # 加这句主要是为了保留被修饰的函数的名字
    def wrap(args):
        if args not in cache:
            cache[args] = function(args)
        return cache[args]

    return wrap


@memory
def memory_recursion(n):
    """
    函数本身依旧是普通的递归求斐波那契, 但是装有修饰器
    :param n:
    :return:
    """
    if n <= 2:
        return n
    else:
        return memory_recursion(n - 1) + memory_recursion(n - 2)


def circle(n):
    """
    循环求斐波那契
    :param n:
    :return:
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b


class Fibonacci:
    """
    自己之前写的一个斐波那契数列
    """

    def __init__(self, f0, f1):
        self.f0 = f0
        self.f1 = f1

    def _fib(self, a, b):
        a = self.f0
        b = self.f1
        yield a
        yield b
        while True:
            a, b = b, a + b
            yield b

    def fib_generator(self):
        """
        生成器
        :return:
        """
        return self._fib(self.f0, self.f1)


if __name__ == "__main__":
    print("方法一: 匿名函数(其实就是递归), 注意这种写法被 PEP8 报警了...")
    # fibonacci_1 = lambda n: n if n <= 2 else fibonacci_1(n - 1) + fibonacci_1(n - 2)
    fibonacci_1 = recursion
    time_cost = timeit.timeit("recursion(33)", setup="from fibonacci import recursion", number=1)
    print("fibonacci_1(33) 耗时: {}".format(time_cost))

    print("方法二: 依旧递归求解, 不过加了个记忆用的修饰器, 速率翻倍了都")
    fibonacci_2 = memory_recursion
    time_cost = timeit.timeit("memory_recursion(33)", setup="from fibonacci import memory_recursion")
    print("fibonacci_2(33) 耗时: {}".format(time_cost))

    print("方法三: 循环求解")
    fibonacci_3 = circle
    time_cost = timeit.timeit("circle(33)", setup="from fibonacci import circle", number=1)
    print("fibonacci_3(33) 耗时: {}".format(time_cost))

    print("方法四: 同样循环求解, 不过是通过生成器实现的")
    fibonacci_4 = Fibonacci(1, 2).fib_generator()
