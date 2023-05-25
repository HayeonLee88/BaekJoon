# 2164번: 카드2
from collections import deque

n = int(input())
q = deque()
q.extend(range(1, n + 1, 1))
while len(q) > 2:
    q.popleft()
    step2 = q.popleft()
    q.append(step2)

answer = q.pop()
print(answer)
