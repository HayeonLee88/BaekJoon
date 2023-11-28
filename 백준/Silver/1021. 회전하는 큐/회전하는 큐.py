import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
q = deque([i for i in range(1, n + 1)])
pop_list = list(map(int, input().split()))

answer = 0
for num in pop_list:
    left_rotate = q.index(num)
    right_rotate = len(q) - left_rotate

    if left_rotate < right_rotate:
        answer += left_rotate
        q.rotate(-left_rotate)
        q.popleft()
    else:
        answer += right_rotate
        q.rotate(right_rotate)
        q.popleft()

print(answer)
