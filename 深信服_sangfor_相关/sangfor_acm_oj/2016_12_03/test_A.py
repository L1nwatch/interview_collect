# coding=utf-8   #默认编码格式为utf-8
import random

if __name__ == "__main__":
    for i in range(100):
        print("{} {}".format(random.randint(1, 100 * 100000000), random.randint(0, 1)))
