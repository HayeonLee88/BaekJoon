'''
4:10~4:16
각 종류 별로 옷을 n가지 입기/안입기 -> n + 1
'''
from collections import defaultdict
def solution(clothes):
    answer = 1
    dict_ = defaultdict(int)
    for name, type_ in clothes:
        dict_[type_] += 1

    for v in dict_.values():
        answer *= (v + 1)
    return answer - 1