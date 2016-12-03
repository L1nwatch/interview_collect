# coding=utf-8   #默认编码格式为utf-8
"""
题目描述
Yiyi is trying to develop an examine system. He finds it not so easy to judge filling question. There may be multiple answers for a blank, For example, The 2008 Olympic games was hold in ____City，The answer can be “Beijing”, and it can also be “Peking”, he made the answer like this: Beijing(Peking), which means that Beijing, Peking are both correct answers; A filling question may have several blanks, For some problems those blanks should be answered in order, for example, The 2000, 2004 Olympic games was hold respectively in ____City and ____City, The answer should be “Sydney Athens”; For other problems those blanks don’t need be answered in order, for example, ACRush has taken part in the ICPC world finals in the year ____ and ____, The answer could be “2007|2009”, and it can also be “2009|2007”. Now you are required to help him to write a program to judge the filling problems.
输入
The first line contains an integer N, indicate the number of problems. The following N*3 lines, each 3 lines indicate a filling problem, the first line is the question, the second line is the answer(There will not be a answer contains ‘|’, ’(‘, ’)’ for every blank, For one problem every neighboring blanks are separated by “|” ), the third line indicate if the blanks should be filled in order, the word “True” means the blanks should be filled in order while “False” means that filling the blanks in order is not necessary. The following line contains an integer M, indicate the number of person, each person will fill all the problems, so there follows N*M lines, each N lines indicate a person’s answer for the N problems (There will not be a answer contains ‘|’, ‘(’, ‘)’ for every blank, For one problem every neighboring blanks are separated by “|” ), according to the sequence of the N problems.
输出
There are M lines, for each person, write the number of blanks he/she filled correctly.
样例输入
3
The 2004, 2008 Olympic games was hold respectively in ____City and ____City.
Athens|Beijing(Peking)
True
ACRush has taken part in the ICPC world finals in the year ____ and ____.
2007|2009
False
Aaaa____bbbb_____.
Ccc(cc)|Ddd(dd)
False
2
Athens|Beijing
2007|2009
Dd|cc
Beijing|Athens
2009|2008
Ddd|cc
样例输出
5
3
"""
import copy


def build_question_and_answer(questions, answers, is_ordered):
    q_a_list = list()

    for question, answer, is_order in zip(questions, answers, is_ordered):
        each_q_a = dict()
        each_q_a["blanks"] = str(question).count("____")
        each_q_a["is_order"] = is_order
        each_q_a["answer"] = list()
        can_be_answer = str(answer).split("|")
        for each_possible_answer in can_be_answer:
            if "(" in each_possible_answer and ")" in each_possible_answer:
                answer1, answer2 = each_possible_answer.split("(")
                each_q_a["answer"].append(answer1)
                each_q_a["answer"].append(str(answer2).strip(")"))
            else:
                each_q_a["answer"].append(each_possible_answer)
            each_q_a["answer"].append("|")
        q_a_list.append(each_q_a)

    return q_a_list


def right_answer_account(order, answer, q_a_list):
    counts = 0

    # 如果没有顺序要求
    person_answer = answer.split("|")
    if q_a_list[order]["is_order"] == "False":
        for each_answer in person_answer:
            if each_answer in q_a_list[order]["answer"]:
                counts += 1
    else:
        # 如果有顺序要求
        right_answers = copy.deepcopy(q_a_list[order]["answer"])  # 注意需要深拷贝
        for each_blank in range(q_a_list[order]["blanks"]):
            answer_of_this_blank = list()

            temp = right_answers.pop(0)
            while temp != "|":
                answer_of_this_blank.append(temp)
                if len(right_answers) > 0:
                    temp = right_answers.pop(0)
                else:
                    break

            if person_answer.pop(0) in answer_of_this_blank:
                counts += 1

    return counts


def solve(question_input):
    number_of_questions = int(question_input.pop(0))
    questions, answers, is_ordered = list(), list(), list()
    for each_question in range(number_of_questions):
        questions.append(question_input.pop(0))
        answers.append(question_input.pop(0))
        is_ordered.append(question_input.pop(0))

    judge_list = build_question_and_answer(questions, answers, is_ordered)

    number_of_person = int(question_input.pop(0))
    results = list()
    for each_person in range(number_of_person):
        counts = 0
        for answer_order in range(number_of_questions):
            counts += right_answer_account(answer_order, question_input.pop(0), judge_list)
        results.append(str(counts))

    return results


if __name__ == "__main__":
    while True:
        try:
            question_input = list()

            n = input()
            question_input.append(n)
            for i in range(n):
                for j in range(3):
                    question_input.append(raw_input())


            m = input()
            question_input.append(m)
            for i in range(m):
                for j in range(n):
                    question_input.append(raw_input())

            for each in solve(question_input):
                print(each)
        except EOFError:
            break
