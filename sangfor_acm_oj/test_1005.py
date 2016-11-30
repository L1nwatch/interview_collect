# coding=utf-8   #默认编码格式为utf-8
import unittest
from acm_1005 import solve


class Test1005(unittest.TestCase):
    def test_answer(self):
        question = ["3", "The 2004, 2008 Olympic games was hold respectively in ____City and ____City.",
                    "Athens|Beijing(Peking)", "True",
                    "ACRush has taken part in the ICPC world finals in the year ____ and ____.",
                    "2007|2009", "False", "Aaaa____bbbb_____.", "Ccc(cc)|Ddd(dd)", "False", "2", "Athens|Beijing",
                    "2007|2009", "Dd|cc", "Beijing|Athens", "2009|2008", "Ddd|cc"]
        answer = ["5", "3"]
        self.assertTrue(answer == solve(question))


if __name__ == "__main__":
    unittest.main()
