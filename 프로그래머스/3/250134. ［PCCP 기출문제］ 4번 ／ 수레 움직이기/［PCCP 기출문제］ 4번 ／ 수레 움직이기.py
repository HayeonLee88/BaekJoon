'''
3:46 ~ 4:53
Backtracking

'''
import sys

sys.setrecursionlimit(100000000)
INF = int(1e9)
answer = INF

def solution(maze):
    n, m = len(maze), len(maze[0])
    visited_red = [[False] * m for _ in range(n)]
    visited_blue = [[False] * m for _ in range(n)]
    red_start = ()
    blue_start = ()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                red_start = (i, j)
                visited_red[i][j] = True
            elif maze[i][j] == 2:
                blue_start = (i, j)
                visited_blue[i][j] = True

    def Backtracking(x1, y1, x2, y2, cnt):
        global answer
        if maze[x1][y1] == 3 and maze[x2][y2] == 4:
            answer = min(answer, cnt)
            return 
        elif maze[x1][y1] == 3:
            for j in range(4):
                nx2 = x2 + dx[j]
                ny2 = y2 + dy[j]
                if nx2 < 0  or nx2 >= n or ny2 < 0 or ny2 >= m:
                    continue
                if maze[nx2][ny2] == 5:
                    continue
                if visited_blue[nx2][ny2]:
                    continue
                if (x1, y1) == (nx2, ny2):
                    continue
                visited_blue[nx2][ny2] = True
                Backtracking(x1, y1, nx2, ny2, cnt + 1)
                visited_blue[nx2][ny2] = False
        elif maze[x2][y2] == 4:
            for i in range(4):
                nx1 = x1 + dx[i]
                ny1 = y1 + dy[i]
                if nx1 < 0  or nx1 >= n or ny1 < 0 or ny1 >= m:
                    continue
                if maze[nx1][ny1] == 5:
                    continue
                if visited_red[nx1][ny1]:
                    continue
                if (nx1, ny1) == (x2, y2):
                    continue
                visited_red[nx1][ny1] =  True
                Backtracking(nx1, ny1, x2, y2, cnt + 1)
                visited_red[nx1][ny1] =  False
        else:
            for i in range(4):
                nx1 = x1 + dx[i]
                ny1 = y1 + dy[i]
                if nx1 < 0  or nx1 >= n or ny1 < 0 or ny1 >= m:
                    continue
                if maze[nx1][ny1] == 5:
                    continue
                if visited_red[nx1][ny1]:
                    continue
                if (nx1, ny1) == (x2, y2):
                    for j in range(4):
                        nx2 = x2 + dx[j]
                        ny2 = y2 + dy[j]
                        if nx2 < 0  or nx2 >= n or ny2 < 0 or ny2 >= m:
                            continue
                        if maze[nx2][ny2] == 5:
                            continue
                        if visited_blue[nx2][ny2]:
                            continue
                        if (nx2, ny2) == (x1, y1):
                            continue
                        if (nx1, ny1) == (nx2, ny2):
                            continue
                        visited_red[nx1][ny1] =  True
                        visited_blue[nx2][ny2] = True
                        Backtracking(nx1, ny1, nx2, ny2, cnt + 1)
                        visited_red[nx1][ny1] =  False
                        visited_blue[nx2][ny2] = False
                        continue
                    continue
                for j in range(4):
                    nx2 = x2 + dx[j]
                    ny2 = y2 + dy[j]
                    if nx2 < 0  or nx2 >= n or ny2 < 0 or ny2 >= m:
                        continue
                    if maze[nx2][ny2] == 5:
                        continue
                    if visited_blue[nx2][ny2]:
                        continue
                    if (nx1, ny1) == (nx2, ny2):
                        continue
                    visited_red[nx1][ny1] =  True
                    visited_blue[nx2][ny2] = True
                    Backtracking(nx1, ny1, nx2, ny2, cnt + 1)
                    visited_red[nx1][ny1] =  False
                    visited_blue[nx2][ny2] = False
        return 
    
    Backtracking(red_start[0], red_start[1], blue_start[0], blue_start[1], 0)
    if answer == INF:
        return 0
    else:
        return answer
