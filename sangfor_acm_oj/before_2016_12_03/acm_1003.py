# coding=utf-8   #默认编码格式为utf-8
"""
定理：把一个至少两位的正整数的个位数字去掉，再从余下的数中减去个位数的5倍。当且仅当差是17的倍数时，原数也是17的倍数 。
例如，34是17的倍数，因为3-20=-17是17的倍数；201不是17的倍数，因为20-5=15不是17的倍数。输入一个正整数n，你的任务是判断它是否是17的倍数。
输入
    输入文件最多包含10组测试数据，每个数据占一行，仅包含一个正整数n（1<=n<=10100），表示待判断的正整数。n=0表示输入结束，你的程序不应当处理这一行。
输出
    对于每组测试数据，输出一行，表示相应的n是否是17的倍数。1表示是，0表示否。

样例输入
    34
    201
    2098765413
    1717171717171717171717171717171717171717171717171718
    0
样例输出
    1
    0
    1
    0
"""


def solve(number):
    result = int(str(number)[:-1]) - int(str(number)[-1]) * 5
    if result % 17 == 0:
        answer = "1"
    else:
        answer = "0"
    return answer


if __name__ == "__main__":
    while True:
        try:
            problem_input = input()
            if problem_input == 0:
                break
            print(solve(problem_input))
        except EOFError:
            break
