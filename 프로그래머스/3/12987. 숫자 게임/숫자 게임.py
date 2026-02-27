'''
8:50~
가장 적은 수 차이로 이기기, 질 때는 큰 수 차이로 지기
아무것도 못 이기는 숫자는 가장 큰 숫자랑 지도록 하기
'''
from collections import deque
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    B_Q = deque(b for b in B)
    A_Q = deque(a for a in A)
    
    while B_Q:
        a = A_Q.popleft()
        b = B_Q.popleft()
        if a < b:
            answer += 1
        else:
            A_Q.appendleft(a)
            A_Q.pop()
    return answer