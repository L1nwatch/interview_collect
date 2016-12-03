# coding=utf-8   #默认编码格式为utf-8
"""
题目描述
对于给定的正整数n，格雷码为满足如下条件的一个编码序列：
(1) 序列由2^n个编码组成，每个编码都是长度为n的二进制位串。
(2) 序列中无相同的编码。
(3) 序列中位置相邻的两个编码恰有一位不同。
例如：n=2时的格雷码为：{00, 01, 11, 10}。

输入
m个测试例的数据，每个测试例的数据由一个正整数n(n <= 20) 组成,以0结束。

输出
对于每个测试例n，输出2^n个长度为n的格雷码。（为方便查看，在每个格雷码内，两个位之间没有空格如，00输出为：00）。两个测试例的输出数据之间用一个空行隔开，最后一个测试例后两个空行。

样例输入
4
5
0
样例输出
0000
0001
0011
0010
0110
0111
0101
0100
1100
1101
1111
1110
1010
1011
1001
1000

00000
00001
00011
00010
00110
00111
00101
00100
01100
01101
01111
01110
01010
01011
01001
01000
11000
11001
11011
11010
11110
11111
11101
11100
10100
10101
10111
10110
10010
10011
10001
10000
"""


def xor(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    return str((number1 + number2) % 2)


def solve(number):
    # 公式：最高位：b[i] = a[i]，其他位：b[i] = a[i] 异或 a[i+1]，a为一个数的二进制表示，b为格雷码表示
    number = int(number)
    answer = list()
    for i in range(2 ** number):
        a = bin(i)[2:].zfill(number)
        result = a[0]
        for i in range(len(a[1:])):
            result += xor(a[i], a[i + 1])
        answer.append(result)

    for each in answer:
        print(each)


if __name__ == "__main__":
    while True:
        try:
            problem_input = input()
            if problem_input == 0:
                break
            solve(problem_input)
            print ""
        except EOFError:
            break
