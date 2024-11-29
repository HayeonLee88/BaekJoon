import sys

input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
array = list(map(int, input().split()))
cnt = [0] * (100001)

answer = 0
start = 0

for end in range(n):
    cnt[array[end]] += 1

    # 슬라이딩 윈도우 조건 확인 및 start 이동
    while cnt[array[end]] > k:
        cnt[array[start]] -= 1
        start += 1

    # 현재 윈도우의 길이를 계산하여 최대값 갱신
    answer = max(answer, end - start + 1)

print(answer)