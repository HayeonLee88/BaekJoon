# 14225번: 부분수열의 합(BrutrForce)
'''
수열 S가 주어졌을 때, 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구하는 프로그램

problem? 첫째 줄에 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 출력

How?
    t 이하의 수를 만들 수 있는지 없는 지 체크한다.
    1. 수열을 오름차순 정렬하여 탐색한다.
    2. t는 1부터 시작한다.
    3. 수열의 값이 t보다 작거나 같으면 t 이하의 수를 만들 수 있다.
    4. 수열의 값이 t보다 크면 t를 만들 수 없기 때문에 종료
'''
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

t = 1
for num in nums:
    if t < num:
        break
    t += num
print(t)