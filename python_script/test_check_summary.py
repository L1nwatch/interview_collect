#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.03.10 作为 check_summary 的测试文件, 具体实现参考博客源码
"""
import unittest
import os
from check_summary import Checker

__author__ = '__L1n__w@tch'


class Tester(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.test_check = Checker()

    def test_get_title_list_from_summary(self):
        """
        测试函数是否获取正确
        """
        summary_path = os.path.join(self.base_dir, "SUMMARY.md")
        title_list = self.test_check.get_all_path_in_summary_md_file(summary_path)

        self.assertIn("README.md", title_list)
        self.assertIn("腾讯 2017 暑期实习生编程题/腾讯 2017 暑期实习生编程题.md", title_list)
        self.assertIn("软件测试题/题目汇总.md", title_list)
        self.assertIn("Python 语言特性/3 类变量和实例变量.md", title_list)
        self.assertIn("Python 面试编程题/13 单链表逆置/单链表逆置.md", title_list)


if __name__ == "__main__":
    pass
