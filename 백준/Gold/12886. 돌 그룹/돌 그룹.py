from collections import deque


a, b, c = map(int, input().split())
total = a + b + c
visited = [[False] * total for _ in range(total)]

q = deque()
q.append((a, b))

def BFS(target):
    while q:
        a, b = q.popleft()
        c = total - (a + b)
        if a == b == target:
            return 1
        for x, y in [(a, b), (a, c), (b, c)]:
            if x == y:
                continue
            if x > y:
                x, y = y, x
            x, y = x + x, y - x 
            min_ = min(x, y)
            max_ = max(x, y)
            if visited[min_][max_]:
                continue
            q.append((min_, max_)) 
            visited[min_][max_] = True
        
    return 0

if total % 3 == 0:
    target = total // 3
    print(BFS(target))
else:
    print(0)