from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]
    
    robot = []
    goal = []
    
    # 로봇 위치와 목표 위치 초기화
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 'R':
                robot = [i, j]
            elif cell == 'G':
                goal = [i, j]
    
    # 이동 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 장애물에 막히거나 끝까지 이동
    def move(x, y, dir):
        while 0 <= x + dx[dir] < n and 0 <= y + dy[dir] < m and board[x + dx[dir]][y + dy[dir]] != 'D':
            x += dx[dir]
            y += dy[dir]
        return x, y
    
    # BFS 탐색
    def bfs():
        q = deque([(robot[0], robot[1], 0)])  # (x, y, 이동 횟수)
        visited[robot[0]][robot[1]] = True
        
        while q:
            x, y, cnt = q.popleft()
            
            # 목표 지점 도달
            if [x, y] == goal:
                return cnt
            
            # 4방향 이동
            for i in range(4):
                nx, ny = move(x, y, i)
                
                # 방문하지 않은 위치라면 큐에 추가
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt + 1))
        
        return -1  # 목표에 도달할 수 없는 경우
    
    return bfs()
