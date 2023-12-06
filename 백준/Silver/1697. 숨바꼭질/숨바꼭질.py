from collections import deque

INF = int(1e9)
n, k = map(int, input().split())

times = [INF] * 100001
times[n] = 0

def bfs(start, target):
    if start == target:
        return 0
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        moving = [now - 1, now + 1, now * 2]
        if now == target:
            break
        for i in range(3):
            nxt = moving[i]
            if nxt < 0 or nxt > 100000:
                continue
            if times[nxt] <= times[now] + 1:
                continue
            else:
                q.append(nxt)
                times[nxt] = times[now] + 1

    return times[target]

print(bfs(n, k))