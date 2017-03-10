#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 实现对指定文件夹下所有文件进行内容搜索, 关键词及搜索的文件类型由用户指定

2016.07.23 由于自己现在记的笔记形式是 GitHub + GitBook, 但是这两货的笔记搜索功能是在有限, 故需要将此程序进一步扩展
2016.06.21 由于微机原理也要进行 ARM 平台小车的开发, 遇到了跟 ZigBee 一样的困境, 需要快速掌握工程文件, 所以还是将这个程序通用化吧
2016.04 起初编写这个程序是由于对协议栈不熟悉, 所以需要对协议栈的每一个文件进行关键词搜索, 同时列举出来
"""
import os
import argparse

__author__ = '__L1n__w@tch'


def is_valid_file_type(name, types):
    """
    :param name: 文件名, 比如 '.DS_Store'
    :param types: 要搜寻的文件类型, 比如 [".h", ".c"]
    :return: False
    """
    name = name.lower()
    for each_type in types:
        if name.endswith(each_type):
            return True
    return False


def add_argument(parser):
    """
    为解析器添加参数
    :param parser: ArgumentParser 实例对象
    :return: None
    """
    parser.add_argument("--path", "-p", type=str,
                        default=os.curdir, help="文件夹路径")
    parser.add_argument("--type", "-t", type=str, default=".c#.h#.cpp#.py#.md",
                        help="搜索文件类型, 默认值及格式为: \".c#.h#.cpp#.py#.md\"")
    parser.add_argument("--keyword", "-k", type=str, default="main", help="要搜索的关键词")


def set_argument(options):
    """
    读取用户输入的参数, 检验是否合法
    :param options: parser.opts
    :return: dict()
    """
    configuration = dict()
    configuration["path"] = options.path
    configuration["file_type"] = options.type.split("#")
    # configuration["keyword"] = options.keyword.lower()

    print("[*] 要搜索的路径为: {}".format(configuration["path"]))
    print("[*] 要搜索的文件类型包括: {}".format(configuration["file_type"]))
    # print("[*] 要搜索的关键词为: {}".format(configuration["keyword"]))

    return configuration


def initialize():
    """
    进行初始化操作, 包括 argparse 解析程序的初始化, 参数的相关设定等
    :return: path, file_type, keyword
    """
    parser = argparse.ArgumentParser(description="文件内容搜索程序")
    add_argument(parser)
    configuration = set_argument(parser.parse_args())

    print("[*] {} 搜索开始 {}".format("-" * 30, "-" * 30))

    return configuration["path"], configuration["file_type"]


def search_keyword_infile(file_path, word):
    """
    判断一个文件内是否含有该关键词, 并且把含有该关键词的那一行返回回去
    :param file_path: 文件路径, 比如 './compare_key.py'
    :param word: "main"
    :return: 返回含有关键词的那一行, 或者返回 None 表示找不到, 即 None or "int main()"
    """
    # word 处理
    word = word.lower()
    word = word.encode("utf8")

    with open(path, "rb") as f:
        data = f.readlines()

    for each_line in data:
        if word in each_line.lower():
            return each_line
    return None


if __name__ == "__main__":
    path, file_type = initialize()
    keyword = input("[?] 请输入要搜索的关键词: ")

    for root, dirs, files in os.walk(path):
        for each_file in files:
            if is_valid_file_type(each_file, file_type):
                path = root + os.sep + each_file
                line_content = search_keyword_infile(path, keyword)
                if line_content:
                    print("[*] Found in \"{}\", path is \033[95m{}\033[0m".format(each_file, path))
                    print("[*] {}\033[91m{}\033[0m".format("\t" * 4, line_content.decode("utf8").strip()))
    print("[*] {} 搜索结束 {}".format("-" * 30, "-" * 30))
