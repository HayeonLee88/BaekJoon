# 12851 숨바꼭질 2 BFS: 너비우선탐색
# 찾는 수와 현재 수가 같은 경우 고려하기
from collections import deque
n, k = map(int, input().split())
graph = [0] * 100001
cnt = 0


def BFS(start, end, count):
    queue = deque([start])
    if start == end:
        count = 1
        return count
    while queue:
        now = queue.popleft()
        next_list = [now-1, now+1, now*2]
        for nxt in next_list:
            if nxt < 0 or nxt > 100000:
                continue
            if not graph[nxt]:
                graph[nxt] = graph[now] + 1
                if nxt == end:
                    count += 1
                    print(f'{count}번째 : {graph[end]}')
                else:
                    queue.append(nxt)
            elif graph[nxt] >= graph[now] + 1: # 작거나 같을 때!
                graph[nxt] = graph[now] + 1
                if nxt == end:
                    count += 1
                    print(f'{count}번째 : {graph[end]}')
                else:
                    queue.append(nxt)
    return count

cnt = BFS(n, k, cnt)
print(graph[k])
print(cnt)
