from functools import reduce

def solution(clothes):
    answer = 0
    dict_ = dict()
    
    for name, category in clothes:
        try:
            dict_[category] += 1
        except KeyError:
            dict_[category] = 2
            
    return reduce(lambda x, y: x * y ,dict_.values()) - 1

