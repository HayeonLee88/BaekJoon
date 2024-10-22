'''
9:43~
BFS
'''
from collections import deque

def solution(begin, target, words):
    answer = 0
    len_ = len(words)
    dict_= {word : words for word in words}
    dict_[begin] = words

    visited = {word : False for word in words}
    visited[begin] = False
    
    q = deque()
    q.append([begin, 0])
    visited[begin] = True
    
    def check(start, end):
        cnt = sum([1 for s, e in zip(start, end) if s != e])
        return cnt == 1
    
    while q:
        now, cnt = q.popleft()
        if now == target:
            answer = cnt
            break
        for i in range(len_):
            nxt = dict_[now][i]
            if not visited[nxt]:
                if check(now, nxt):
                    q.append([nxt, cnt + 1])
                    visited[nxt] = True
    return answer