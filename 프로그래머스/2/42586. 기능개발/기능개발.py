from collections import deque

def solution(progresses, speeds):
    answer = []
    len_ = len(speeds)
    pro = deque(x for x in progresses)
    spd = deque(x for x in speeds)
    
    while spd:
        for i in range(len_):
            pro[i] += spd[i]
            
        tmp = 0
        for _ in range(len_):
            now = pro.popleft()
            if now < 100:
                pro.appendleft(now)
                break
            spd.popleft()
            tmp += 1
            
        if tmp > 0:
            answer.append(tmp)
            len_ = len(spd)
            
    return answer