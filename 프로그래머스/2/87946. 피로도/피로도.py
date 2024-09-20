from itertools import permutations

def solution(k, dungeons):
    answer = -1
    pmttns = list(permutations(dungeons, len(dungeons)))
    
    for pmttn in pmttns:
        tmp = k
        for i, (min_p, use_p) in enumerate(pmttn):
            if tmp < min_p:
                break
            tmp -= use_p
            answer = max(answer, i + 1)
        if answer == len(dungeons):
            break

    return answer