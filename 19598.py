# 19598번: 최소 회의실 개수 (최소 힙, 정렬)
'''
N: 회의 개수 (1 ≤ N ≤ 100,000)

problme: 회의 시작과 끝 시간이 주어질 때 회의를 모두 진행할 수 있는 최소 회의실 개수를 구하라

How?
    시작 시간이 빠른 회의부터 정렬하고, 회의 끝 시간이 빠른 순으로 진행 중인 회의실 최소힙을 만든다.
    최소힙을 사용하여 회의 끝시간이 빠른 회의와 다음 회의 시작 시간을 비교한다.
    이때 회의 시작 시간보다 진행중인 회의의 끝 시간이 더 느리다면 새로운 회의실 추가 heappush
    시간이 같거나 작다면 heapreplace
'''
import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
meetings = [] # [시작시간, 끝 시간] 담는 리스트 초기화
progress = [] # 끝시간을 담는 최소힙 초기화
for i in range(n):
    m = list(map(int, input().split()))
    meetings.append(m)

meetings.sort() # 시작시간을 기준으로 회의들 정렬

heapq.heappush(progress, meetings[0][1])
for i in range(1, n):
    s, e = meetings[i]
    if progress[0] <= s: # 회의 진행 중인 회의실이 있다면 그 회의의 끝 시간과 다음 시작하는 회의 시간을 비교
        heapq.heapreplace(progress, e) # 끝 시간 <= 시작 시간이라면 replace
    else: # 회의실 추가
        heapq.heappush(progress, e)

print(len(progress))