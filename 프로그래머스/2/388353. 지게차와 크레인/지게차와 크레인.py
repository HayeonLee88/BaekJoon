from collections import deque

def solution(storage, requests):
    n, m = len(storage), len(storage[0])    
    new_storage = [['1'] * (m + 2) for _ in range(n + 2)]
    # 빈공간
    empty = deque()
    # 외부 공간
    outside = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            new_storage[i][j] = storage[i - 1][j - 1]
    for i in range(n + 2):
        if i in [0, n + 1]:
            for j in range(m + 2):
                outside.append((i, j))
        else:
            outside.append((i, 0))
            outside.append((i, m + 1))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    
    def bfs(target):
        cnt = 0
        visited = [[False] * (m + 2) for _ in range(n + 2)]
        q = deque()
        for x, y in outside:
            q.append((x, y))
            visited[x][y] = True     
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 1 or nx > n or ny < 1 or ny > m:
                    continue
                if visited[nx][ny]:
                    continue
                if new_storage[nx][ny] == target:
                    visited[nx][ny] = True
                    # 외부와 연결된 곳이기 때문에 외부로 바꾸기
                    new_storage[nx][ny] = '1'
                    outside.append((nx, ny))
                    cnt += 1
        return cnt
    
    def check_is_outside():
        while empty:
            changed = False
            for _ in range(len(empty)):
                check = False
                x, y = empty.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if new_storage[nx][ny] == '1':
                        new_storage[x][y] = '1'
                        outside.append((x, y))
                        check = True
                        changed = True
                        break
                if not check:
                    empty.append((x, y))
            if not changed:
                break
                
                
    answer = n * m
    for request in requests:
        if len(request) == 1:
            answer -= bfs(request)
        else:
            target = request[0]
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if new_storage[i][j] == target:
                        answer -= 1
                        empty.append((i, j))
                        new_storage[i][j] = '0'
        check_is_outside()

    return answer
