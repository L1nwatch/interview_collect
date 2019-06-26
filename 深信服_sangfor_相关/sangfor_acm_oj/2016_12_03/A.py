# coding=utf-8   #默认编码格式为utf-8
import sys

def solve(question_list, t):
    sum_all = 0
    for each in question_list:
        p, s = each.split(" ")
        if s == "0":
            # no
            sum_all += int(p) * 2
        else:
            sum_all += int(p) * t

    print("{}".format(sum_all))


if __name__ == "__main__":
    with open("test_A.txt", "r") as f:
        sys.stdin = f

        while True:
            try:
                n = input()
                if n == 0:
                    break
                else:
                    question = list()
                    for i in range(n):
                        question.append(raw_input().strip())
                    t = input()
                    solve(question, t)
            except EOFError:
                break
