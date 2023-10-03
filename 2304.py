# 2304번: 창고 다각형 (BruteForce, Stack)

'''
- 올라갔다 내려가는 모양
- 계속 올라가는 모양
- 계속 내려가는 모양
제일 높은 기둥을 기준으로 1. 그 앞은 점점 높아져야 하고 2.그 뒤는  점점 낮아져야 한다.
1. 앞보다 뒤가 높은 기둥만 담기
2. 뒤보다 앞이 더 높은 기둥의 높이만 담기

기둥 개수: N, 1 이상 1,000 이하
N개의 줄에 왼쪽 면의 위치 L과 높이 정수 H, L과 H는 둘 다 1 이상 1,000 이하
위치 순으로 입력되지 않음 -> L 최대 1000개 이므로 모든 범위를 담는 리스트 생성
제일 높음 H 위치 찾기
'''
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
tops = [0] * 1001
highest= (0, 0)
answer = 0

for i in range(n):
    l, h = map(int, input().split())
    tops[l] = h
    if h > highest[1]:
        highest = (l, h)

def check_high(top, former_top):
    global answer
    if top < former_top:
        answer += former_top
        top = former_top
    else:
        answer += top
        former_top = top

    return answer, top, former_top

tmp = 0 # 이전 탑의 높이
for i in range(0, highest[0] + 1):
    answer, now, tmp =  check_high(tops[i], tmp)

tmp = 0 # 이후 탑의 높이 (현재 l보다 큰 위치에 있는 높이)
for i in range(1000, highest[0], -1):
    answer, now, tmp =  check_high(tops[i], tmp)

print(answer)