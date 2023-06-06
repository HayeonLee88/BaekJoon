# 2108번: 통계학
'''
1. 산술 평균: N개의 수들의 합을 N으로 나눔 round(sum() / n)
2. 중앙값: 오름차순 정렬 ->  n//2번째에 있는 수
3. 최빈값: N개의 수 중 가장 많이 나타나는 값 -> counter or 리스트로 개수
        => 여러개 있을 경우 최빈값 중 두 번째로 작은 값 출력
4. 범위: N개의 수들 중 최댓값과 최솟값 차이 max()-min()
수의 개수 N(1 ≤ N ≤ 500,000) N은 홀수
입력된 정수의 절대값은 4,000 미만
'''
import sys
from collections import Counter

n = int(input())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))

print(round(sum(nums) / n))  # 산술평균
nums.sort() # 오름차순 정렬
print(nums[n // 2])  # 중앙값
frequent = list(Counter(nums).items()) # 각 숫자들의 빈도를 알아보기
frequent.sort(reverse=True, key=lambda x: x[1]) # 빈도를 기준으로 내림차순
# n이 1일 때를 고려해야함
print(frequent[0][0] if n == 1 or frequent[0][1] != frequent[1][1] else frequent[1][0])  # 최빈값
print(nums[-1] - nums[0])  # 범위
