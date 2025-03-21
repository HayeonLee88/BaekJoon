'''
9:9~
'''
def solution(answers):
    answer = []
    scores = [0, 0, 0]
    len_ = len(answers)
    one = [1, 2, 3, 4, 5] # 5개: 0~4
    two = [2, 1, 2, 3, 2, 4, 2, 5] # 8개: 0~8
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10개: 0~9
    
    for i in range(len_):
        now = answers[i]
        if one[i % 5] == now:
            scores[0] += 1
        if two[i % 8] == now:
            scores[1] += 1
        if three[i % 10] == now:
            scores[2] += 1
            
    max_ = max(scores)
    if max_ == scores[0]:
        answer.append(1)
    if max_ == scores[1]:
        answer.append(2)
    if max_ == scores[2]:
        answer.append(3)
        
    return sorted(answer)