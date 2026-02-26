'''
10:35~11:10
각 곡갱이는 5개의 연속된 광물을 캘 수 있음
'''
from collections import deque

def solution(picks, minerals):
    answer = 0
    health = {('diamond', 'diamond'): 1, ('diamond', 'iron'): 1, ('diamond', 'stone'): 1,
              ('iron', 'diamond'): 5, ('iron', 'iron'): 1, ('iron', 'stone'): 1,
              ('stone', 'diamond'): 25, ('stone', 'iron'): 5, ('stone', 'stone'): 1}
    picks_list = ['diamond'] * picks[0] + ['iron'] * picks[1] + ['stone'] * picks[2]
    max_ = min(sum(picks * 5), len(minerals))
    groups = [minerals[i: i + 5] for i in range(0, max_, 5)]
    groups.sort(reverse=True,
                key=lambda group: (sum(1 for mineral in group if mineral == 'diamond'),
                                   sum(1 for mineral in group if mineral == 'iron'),
                                   sum(1 for mineral in group if mineral == 'stone')))
    
    for idx, group in enumerate(groups):
        for mineral in group:
            answer += health[(picks_list[idx], mineral)]    
    
    return answer