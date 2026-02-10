'''
8:55~45
직사각형의 가장자리 테두리를 따라 움직임
직사각형 내부 먼저 체크: 2
직사각형 내부가 아닌 가장자리 체크: 1
'''
from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 이동 경로를 나타내는 graph 리스트
    graph = [[0] * 101 for _ in range(101)]
    INF = 1e9
    # 개선된 마킹 로직
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 2 # 확실한 내부는 2
                elif graph[i][j] != 2:
                    graph[i][j] = 1 # 이미 내부(2)로 판정된 곳이 아닐 때만 테두리(1)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    dist = 0
    q = deque()
    q.append([characterX * 2, characterY * 2, dist])
    
    while q:
        x, y, dist = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = dist // 2
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프 바깥 체크
            if 0 > nx or nx > 100 or 0 > ny or ny > 100:
                continue
            # 직사각형 내부가 아닌 가장자리만 이동
            if graph[nx][ny] == 1:
                q.append([nx, ny, dist + 1])
                graph[nx][ny] = 2
                
    return answer