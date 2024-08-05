import sys
from collections import deque

input = lambda:sys.stdin.readline().rstrip()

n = int(input())
# 보드
graph = [[-1] * (n + 2)]

for i in range(1, n + 1):
    graph.append([-1])
    graph[i].extend([0] * n)
    graph[i].append(-1)

graph.append([-1] * (n + 2))

# 사과 위치 
k = int(input())
for i in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1

l = int(input())
# 방향 전환 정보
dirs = deque(list(input().split()) for _ in range(l))

# 이동 방향 (오른쪽부터 시계방향)
dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]

dir = {'L': -1, 'D': 1}

def dos(x, y):
    q = deque()
    q.append((1, 1))
    cnt = 0 # 시간
    idx = 0 # 이동방향 인덱스
    x, y = q[0]
    while True:
        cnt += 1
        nx = x + dx[idx]
        ny = y + dy[idx]
        if (nx, ny) in q or graph[nx][ny] == -1:
            break
        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
        else:
            q.popleft()
        q.append((nx, ny))
        x, y = nx, ny
        if dirs:
            if cnt == int(dirs[0][0]):
                _, c = dirs.popleft()
                idx += dir[c]
                idx %= 4
    return cnt

print(dos(1, 1))