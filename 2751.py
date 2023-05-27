# 2751번: 수 정렬하기 2
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
for num in nums:
    print(num)