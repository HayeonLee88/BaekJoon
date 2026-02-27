'''
5:05~
'''

def solution(gems):
    len_ = len(gems)
    gems_dict = {}
    p2 = 0
    min_len = len_ + 1
    gem_cnt = len(set(gems))
    
    answer = [1, min_len]
    for p1 in range(len_):
        gem = gems[p1]
        # 보석이 있으면 (보석 갯수 + 1) 없으면 (0 + 1)
        gems_dict[gem] = gems_dict.get(gem, 0) + 1
        while len(gems_dict) == gem_cnt:
            if p1 - p2 < min_len:
                min_len = p1 - p2
                answer = [p2 + 1, p1 + 1]
            p2_gem = gems[p2]
            gems_dict[p2_gem] -= 1
            if gems_dict[p2_gem] == 0:
                del gems_dict[p2_gem]
            p2 += 1
    
    return answer