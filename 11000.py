# 11000번: 강의실 배정(우선순위 큐)
'''
N: 수업의 개수 (1 ≤ N ≤ 200,000)
Si, Ti: 수업 시작시간, 종료시간 (0 ≤ Si < Ti ≤ 10**9)
* 수업이 끝난 직후 다음 수업 시작 O (Ti ≤ Sj 일 경우 i 수업과 j 수업 같이 들을 수 O)

problem? 모든 수업을 가능하게 할 강의실의 개수를 출력하라

How?
    lecture: 강의 시작, 종료 시간을 담는 리스트, 강의 시작 시간을 기준으로 오름차순 정렬
    rooms: 우선순위 큐, 강의실을 사용하는 강의들의 끝나는 시간을 오름차순 정렬
        1. 처음으로 시작하는 강의의 종료 시간을 rooms에 저장
        2. 이후 강의들을 순차적으로 탐색한다.
        3. 강의 시작 시작이 rooms에서 수업이 가장 빨리 끝나는 시간보다 크거나, 같으면 강의 종료시간과 heapreplace
        4. 강의 시작 시작이 rooms에서 수업이 가장 빨리 끝나는 시간보다 작다면, 강의 종료 시간 heqppush

'''
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
