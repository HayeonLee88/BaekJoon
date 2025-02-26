import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1, 0]  # 제자리 포함 (움직이지 않는 경우 추가)
dy = [0, 0, -1, 1, -1, 1, -1, 1, 0]

def BFS(graph):
    q = deque()
    q.append((7, 0))  # 시작 위치
    walls = deque()

    # 벽의 초기 위치 저장
    for i in range(8):
        for j in range(8):
            if graph[i][j] == '#':
                walls.append((i, j))

    while q:
        size = len(q)
        visited = set()  # 방문 기록
        
        for _ in range(size):  # 한 턴에 이동 가능한 모든 경우를 처리
            x, y = q.popleft()
            
            if (x, y) in walls:  # 벽과 겹치면 패스
                continue
            
            if (x, y) == (0, 7):  # 도착지 도달
                return 1
            
            for i in range(9):  # 8방향 + 제자리 유지
                nx, ny = x + dx[i], y + dy[i]
                
                if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in walls and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))  # 중복 방문 방지

        # 벽 이동 (한 턴이 끝난 후 이동)
        new_walls = deque()
        while walls:
            r, c = walls.popleft()
            if r + 1 < 8:  # 벽이 아래로 이동
                new_walls.append((r + 1, c))
        
        walls = new_walls  # 벽 업데이트

    return 0  # 도착 불가능

# 입력 처리
graph = [list(input().strip()) for _ in range(8)]
print(BFS(graph))
