# -*- coding: utf-8 -*-
import sys

def change_hour(hour, limit):
    hour = str(hour)

    if limit == 12:
        # 改变 0
        for each in range(0, 10):
            try_change = "{}{}".format(each, hour[1])
            if 1 <= int(try_change) <= limit:
                return try_change

        # 改变 1
        for each in range(1, 10):
            try_change = "{}{}".format(hour[0], each)
            if 1 <= int(try_change) <= limit:
                return try_change
    else:
        # 改变 0
        for each in range(0, 10):
            try_change = "{}{}".format(each, hour[1])
            if 0 <= int(try_change) < limit:
                return try_change

        # 改变 1
        for each in range(0, 10):
            try_change = "{}{}".format(hour[0], each)
            if 0 <= int(try_change) < limit:
                return try_change


def change_minute(hour, minute, limit):
    minute = str(minute)
    # minute < 59
    # 改变 0
    for each in range(0, 10):
        try_change = "{}{}".format(each, minute[1])
        if 0 <= int(try_change) <= 59:
            return try_change

    # 改变 1
    for each in range(0, 10):
        try_change = "{}{}".format(minute[0], each)
        if 0 <= int(try_change) <= 59:
            return try_change


def deal_24(time):
    hour, minute = time.split(":")
    hour, minute = int(hour), int(minute)

    if hour < 24 and minute > 59:
        minute = change_minute(hour, minute, 24)
    elif hour < 24 and minute == 59:
        pass
    elif hour < 24 and minute < 59:
        pass
    elif hour == 24 and minute > 59:
        hour = 23
        minute = change_minute(hour, minute, 24)
    elif hour == 24 and 0 <= minute <= 59:
        hour = 23
    elif hour > 24 and minute > 59:
        hour = change_hour(hour, 24)
        minute = change_minute(hour, minute, 24)
    elif hour > 24 and minute <= 59:
        hour = change_hour(hour, 24)

    return "{}:{}".format(str(hour).zfill(2), str(minute).zfill(2))


def deal_12(time):
    hour, minute = time.split(":")
    hour, minute = int(hour), int(minute)

    if hour == 0 and minute > 59:
        hour = 1
        minute = change_minute(hour, minute, 12)
    elif hour == 0 and minute == 59:
        hour = 1
    elif hour == 0 and minute < 59:
        hour = 1
    elif 0 < hour <= 12 and minute > 59:
        minute = change_minute(hour, minute, 12)
    elif 0 < hour <= 12 and minute == 59:
        pass
    elif 0 < hour <= 12 and minute < 59:
        pass
    elif hour == 13 and minute > 59:
        hour = 12
        minute = change_minute(hour, minute, 12)
    elif hour == 13 and 0 <= minute <= 59:
        hour = 12
    elif hour > 13 and minute > 59:
        hour = change_hour(hour, 12)
        minute = change_minute(hour, minute, 12)
    elif hour > 13 and minute <= 59:
        hour = change_hour(hour, 12)

    return "{}:{}".format(str(hour).zfill(2), str(minute).zfill(2))


def solve(n, time):
    if n == 24:
        return deal_24(time)
    else:
        return deal_12(time)


if __name__ == "__main__":
    with open("test_C.txt", "r") as f:
        sys.stdin = f

        with open("test_C_answer.txt", "w") as f1:
            while True:
                try:
                    n = int(input())
                    # n = input()
                    # time = raw_input()
                    time = input()
                    # print(solve(n, time))
                    print("{}小时,原来={},自己的答案={}".format(n, time, solve(n, time)), file=f1)
                except EOFError:
                    break
