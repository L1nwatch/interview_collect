# coding=utf-8   #默认编码格式为utf-8
import unittest
from acm_1003 import solve


class Test1003(unittest.TestCase):
    def test_answer(self):
        question = ["34", "201", "2098765413", "1717171717171717171717171717171717171717171717171718"]
        answer = ["1", "0", "1", "0"]
        my_solve = [solve(x) for x in question]
        self.assertTrue(all(right_answer == my_answer for right_answer, my_answer in zip(answer, my_solve)))


if __name__ == "__main__":
    unittest.main()
