'''
9:42 ~ 10:00

Dijkstra 
'''
import heapq

INF = int(1e9)
def solution(board):
    answer = 0
    n, m = len(board), len(board[0])
    # cost[x][y][dir] : (x, y)에 dir 방향으로 도착했을 때 최소 비용
    cost = [[[INF] * 4 for _ in range(m)] for _ in range(n)]
    # 최소힙 (cost, pos_idx, (x, y))
    h = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
        
    heapq.heappush(h, (0, 1, (0, 0)))
    heapq.heappush(h, (0, 3, (0, 0)))
    cost[0][0][1] = 0
    cost[0][0][3] = 0
    while h:
        prev_cost, pos, (x, y) = heapq.heappop(h)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny]:
                continue
            now_cost = 100 if i == pos else 600
            if cost[nx][ny][i] <= prev_cost + now_cost:
                continue
            cost[nx][ny][i] = prev_cost + now_cost
            heapq.heappush(h, (cost[nx][ny][i], i, (nx, ny)))
    
    answer = min(cost[-1][-1])
    return answer