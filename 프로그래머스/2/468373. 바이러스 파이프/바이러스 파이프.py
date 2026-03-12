'''
8:49~
시뮬레이션으로 구현?
'''
from collections import deque, defaultdict
def solution(n, infection, edges, k):
    answer = 0
    pipe_type = defaultdict(set)
    infections = set()
    infections.add(infection)
    total_type = set()

    def make_type(tmp):
        if len(tmp) == k:
            total_type.add(tuple(tmp))
            return True
        for t in [1, 2, 3]:
            if tmp and tmp[-1] == t:
                continue
            make_type(tmp + [t])
        return True
    
    make_type([])
            
    for a, b, t in edges:
        pipe_type[t].add((a, b))

    def open_pipe(pipe):
        changed = True
        while changed:
            changed = False
            for a, b in pipe_type[pipe]:
                if a in infections or b in infections:
                    before = len(infections)
                    infections.add(a)
                    infections.add(b)
                    if len(infections) > before:
                        changed = True  
                        
                        
    for types in total_type:
        infections = set()
        infections.add(infection)
        for t in types:
            open_pipe(t)
        answer = max(answer, len(infections))        
        
    return answer