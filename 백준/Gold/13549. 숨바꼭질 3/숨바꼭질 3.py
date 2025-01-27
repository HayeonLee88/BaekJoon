from collections import deque
graph = [-1] * 100001
n, k = map(int, input().split())

def BFS(start, end):
    q = deque([start])
    graph[start] = 0
    while q:
        now = q.popleft()
        move_list = [(1, now - 1), (1, now + 1), (0, now * 2)]
        for move in move_list:
            time, next_node = move
            if next_node < 0 or next_node > 100000:
                continue
            tmp = graph[next_node]
            if tmp == -1 or tmp > graph[now] + time: # 같은 경우를 뺴야 함 최솟 값만 구하는 것이기 때문
                graph[next_node] = graph[now] + time
                if next_node == end:
                    continue
                q.append(next_node)
    return graph[end]

print(BFS(n, k))