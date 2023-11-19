from collections import deque

n, k = map(int, input().split())
circle = deque(i for i in range(1, n + 1))
k = 1 - k

answer = []
while circle:
    circle.rotate(k)
    answer.append(circle.popleft())

answer = '<' +', '.join(str(d) for d in answer) + '>'
print(answer)