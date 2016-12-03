#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python2.X
"""
题目描述
编写程序。实现根据用户输入的三角形的边长，判定是何种三角形。

输入
输入三个数（用逗号隔开），分别代表三角形的三条边。

输出
 /*判断三边是否构成三角形*/
 {
　　/*如果三条边均相等，则输出为等边三角形：   printf("Equilateral triangle\n"); */
　　else 　/*如果只有两条边相等，则输出为等腰三角形：printf("Isoceles triangle\n")*/
           　　else 　/*如果两边的平方和等于第三边平方，则输出为直角三角形：printf("Right-angled triangle\n")  */
                    　　　　　else   /*输出为一般三角形：printf("General triangle\n");*/
 }
 else
        /*输出不能构成三角形：printf("Can't make up of triangle\n"); */

样例输入
3,4,5
样例输出
Right-angled triangle
"""
import string

__author__ = '__L1n__w@tch'


def solve(question):
    a, b, c = question.split(",")
    a, b, c = int(a), int(b), int(c)
    if (a + b > c) and (a - b < c):
        if a == b == c:
            return "Equilateral triangle"
        elif (a == b and a != c) or (a == c and a != b) or (b == c and a != b):
            return "Isoceles triangle"
        elif a ** 2 + b ** 2 == c ** 2:
            return "Right-angled triangle"
        else:
            return "General triangle"
    else:
        return "Can't make up of triangle"


if __name__ == "__main__":
    while True:
        try:
            problem_input = raw_input()
            print solve(problem_input)
        except EOFError:
            break
