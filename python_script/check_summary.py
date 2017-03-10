#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.03.10 使用博客搜索本仓库下某个文件夹的笔记才发现, 存在 summary.md 与路径对应不上的问题, 于是编写脚本来检查
"""
import os
import re

__author__ = '__L1n__w@tch'


class Checker:
    def run(self, summary_md_file_path, root_path):
        """
        进行所有检查
        :param summary_md_file_path: str(), 比如 "SUMMARY.md", 表示 SUMMARY.md 的路径
        :param root_path: str(), 比如 "/Users/.../interview_collect", 表示所有 md 文件的根路径
        :return: None
        """
        # 打开 summary.md, 加载所有目录对应的路径
        path_list = self.get_all_path_in_summary_md_file(summary_md_file_path)

        # 遍历每个路径, 看对应的文件是否存在
        for each_path in path_list:
            if not os.path.exists(os.path.join(root_path, each_path)):
                print("[-] Error: 路径 {} 不存在".format(each_path))

    @staticmethod
    def get_all_path_in_summary_md_file(md_file_path):
        """
        通过读取 summary.md 提取出所有要进行判定的路径
        :param md_file_path: str(), 比如 "SUMMARY.md", 指定 SUMMARY.md 的路径
        :return: list(), 比如 ["README.md", "腾讯 2017 暑期实习生编程题/腾讯 2017 暑期实习生编程题.md", ...]
        """
        result_list = list()
        title_re = re.compile("\[.*\]\((.*)\)")

        with open(md_file_path, "r") as f:
            for each_line in f:
                re_result = title_re.findall(each_line)
                if re_result:
                    result_list.append(re_result[0])

        return result_list


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    summary_path = os.path.join(base_dir, "SUMMARY.md")

    check = Checker()
    check.run(summary_path, base_dir)
