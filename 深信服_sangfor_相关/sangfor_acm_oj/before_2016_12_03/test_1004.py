# coding=utf-8   #默认编码格式为utf-8
import unittest
from acm_1004 import solve, xor


class Test1003(unittest.TestCase):
    def test_answer(self):
        question = ["4", "5", "0"]
        answer = [["0000", "0001", "0011", "0010", "0110", "0111", "0101", "0100", "1100", "1101", "1111", "1110",
                   "1010", "1011", "1001", "1000"],
                  ["00000", "00001", "00011", "00010", "00110", "00111", "00101", "00100", "01100", "01101", "01111",
                   "01110", "01010", "01011", "01001", "01000", "11000", "11001", "11011", "11010", "11110", "11111",
                   "11101", "11100", "10100", "10101", "10111", "10110", "10010", "10011", "10001", "10000"]]
        for i in range(len(answer)):
            self.assertTrue(solve(question[i]) == answer[i])

    def test_xor(self):
        self.assertTrue(xor("1", "1") == "0")
        self.assertTrue(xor("1", "0") == "1")
        self.assertTrue(xor("0", "1") == "1")
        self.assertTrue(xor("0", "0") == "0")


if __name__ == "__main__":
    unittest.main()
