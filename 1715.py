# 1715번: 카드 정렬하기
'''
N개의 숫자 카드 묶음의 각각의 크기가 주어질 떄, 최소한 몇 번의 비교가 필요한지 구하라
N: 1이상 100,000이하
숫자 카드 묶음의 크기: 1,000이하
제일 작은 두 카드 묶음을 합하고 새로운 카드 묶음 추가
    -> 카드 묶음이 남지 않을 때까지 더하기
'''
import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nums = []

for i in range(n):
    num = int(input())
    heapq.heappush(nums, num) # 카드 묶음을 우선순위 큐로 담기

result = 0
while len(nums) >= 2:
    # 가장 작은 두 카드 묶음 빼기
    num1 = heapq.heappop(nums)
    num2 = heapq.heappop(nums)
    new = num1 + num2
    result += new
    heapq.heappush(nums, new) # 새로운 카드 묶음 추가하기
print(result)
