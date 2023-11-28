#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    answer = []
    if my_list:
        for item in my_list:
            if item % 2 == 0:
                answer.append(True)
            else:
                answer.append(False)
    return answer
