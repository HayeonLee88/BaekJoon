# 18310번: 안테나
'''
특정 위치의 집에 한 개의 안테나 설치
    효율성
    - 안테나로부터 모든 집까지의 거리의 총 합이 최소가 되도록
안테나는 집이 있는 곳에만 설치 가능 & 동일한 위치에 여러 개의 집이 존재할 수 O
집의 수 N 1이상 200,000이하
위치 1이상 100,000이하
정렬하여 중간 위치에 있는 값을 정답으로
'''
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
houses = list(map(int, input().split()))
houses.sort()
print(houses[n // 2 - 1] if n % 2 == 0 else houses[n // 2])
