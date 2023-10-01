# 2304번: 창고 다각형 (BruteForce, Stack)

'''
1. 지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
2. 지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
3. 지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
4. 지붕의 가장자리는 땅에 닿아야 한다.
5. 비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.
5번에 따른 지붕의 모양
 1. 높아지다 낮아지기
 2. 계속 높아지기
 3. 계속 낮아지기
 cf) 낮아지다 높아질 순 없다.

 문제.  창고 다각형의 면적이 가장 작은 창고를 만들기
 입력 첫 줄 N(1<=N<=1000), 이후 N줄 동안 (L, H) (1<=L, H<=1000)
 Answer 정수로 창고 다각형의 면적 출력하기
'''
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

stack = deque()
answer = 0
n = int(input())
for i in range(n):
    l, h = map(int, input().split())
    stack.append([h, l]) # 창고의 [높이, 위치]

stack = sorted(stack, key=lambda s: s[1]) # 위치 순으로 정렬
heighest = max(stack)[1] # 가장 높은 기둥의 위치
range_l = [0 for _ in range(1001)] # 모든 위치를 담는 리스트 초기화

for h, l in stack: # 기둥이 있는 위치의 높이 초기화
    range_l[l] = h

# 첫 기둥에서 가장 높은 기둥까지 계속 높아지는 기둥만 담기
tmp = 0
for i in range(stack[0][1], heighest + 1):
    now = range_l[i]
    if tmp <= now: # 이전의 기둥보다 높거나 같다면
        tmp = now # 현재 높이로 초기화
    else: # 이전 기둥보다 낮다면 이전 기둥의 높이로 담기
        range_l[i] = tmp

tmp = stack[-1][0] # 제일 마지막 기둥의 높이로 초기화
# 마지막 기둥에서 제일 높은 기둥 전까지 계속 높아지는 기둥만 담기
for i in range(stack[-1][1], heighest, -1):
    now = range_l[i]
    if tmp <= now: # 현재 기둥이 뒤에 위치한 기둥보다 높다면
        tmp = now # 현재 높이로 초기화
    else: # 뒤에 있는 기둥보다 낮다면 뒷 기둥 높이로 담기
        range_l[i] = tmp

print(sum(range_l[stack[0][1]:stack[-1][1] + 1])) # 기둥이 있는 범위의 지붕 높이 더하기
