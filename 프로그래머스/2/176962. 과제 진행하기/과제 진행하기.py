from collections import deque
def solution(plans):
    answer = []
    
    for i, (name, start, playtime) in enumerate(plans):
        new = int(start[:2]) * 60 + int(start[-2:])
        plans[i][1] = new
        

    plans.sort(key = lambda x: x[1])
    plans = deque(plans)
    stack = []
    
    now = 0
    cnt = 0
    while plans or stack:
        if stack:
            if stack[-1][1] == cnt:
                name, _ = stack.pop()
                answer.append(name)
                cnt = 0
                
        if plans:        
            if plans[0][1] == now:
                if stack:
                    if stack[-1][1] - cnt > 0:
                        stack[-1][1] -= cnt
                    else:
                        name, _ = stack.pop()
                        answer.append(name)
                        
                name, start, playtime = plans.popleft()
                stack.append([name, int(playtime)])
                cnt = 0
                
        now += 1
        cnt += 1
        
    return answer