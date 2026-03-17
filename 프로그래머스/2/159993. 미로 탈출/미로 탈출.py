'''
3:11~24
'''
from collections import deque
import heapq
def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    start_pos = ()
    lever_pos = ()
    exit_pos = ()
    visited = [[False] * m for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start_pos = (i, j)
            elif maps[i][j] == 'L':
                lever_pos = (i, j)
            elif maps[i][j] == 'E':
                exit_pos = (i, j)
    
    def Djikstra(start, target):
        cnt = 0
        h = []
        heapq.heappush(h, (cnt, start))
        visited[start[0]][start[1]] = True
        while h:
            cnt, (x, y) = heapq.heappop(h)
            if (x, y) == target:
                return cnt
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[nx][ny] == 'X':
                    continue
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                heapq.heappush(h, (cnt + 1, (nx, ny)))
        return False
    
    start2lever = Djikstra(start_pos, lever_pos)
    if start2lever:
        visited = [[False] * m for _ in range(n)]
        lever2exit = Djikstra(lever_pos, exit_pos)
        if lever2exit:
            answer = start2lever + lever2exit

    return answer