import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

lecture = []
n = int(input())
for i in range(n):
    s, t = map(int, input().split())
    lecture.append([s, t])

lecture.sort(key=lambda x: x[0])

rooms = []
heapq.heappush(rooms,lecture[0][1])
for i in range(1, n):
    s, t = lecture[i]
    if rooms[0] <= s:
        heapq.heapreplace(rooms, t)
    else:
        heapq.heappush(rooms, t)

print(len(rooms))