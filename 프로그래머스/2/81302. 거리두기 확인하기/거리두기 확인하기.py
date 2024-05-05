from collections import deque

def solution(places):
    answer = [1, 1, 1, 1, 1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs(p, x, y):
        cnt = 0
        q = deque()
        q.append((x, y, False))
        dist[x][y] = cnt
        visited[x][y] = True
        while q:
            x, y, check = q.popleft()
            cnt = dist[x][y] + 1
            if cnt == 3:
                break
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx > 4 or ny < 0 or ny > 4 or places[p][nx][ny] == "X" or visited[nx][ny]:
                    continue
                if places[p][nx][ny] == "P":
                    return 0
                q.append((nx, ny, check))
                dist[nx][ny] = cnt
                visited[nx][ny] = True
        return 1   
    
    for i in range(5):
        dist = [[0] * 5 for _ in range(5)]
        visited = [[False] * 5 for _ in range(5)]
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == "P":
                    answer[i] = bfs(i, j, k)
                    if answer[i] == 0:
                        break
            if answer[i] == 0:
                break
    return answer