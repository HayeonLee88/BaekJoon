import sys

input = lambda:sys.stdin.readline().rstrip()

n = int(input())
values = list(map(int, input().split()))

values.sort()

start, end = 0, n - 1
closest_sum = 2000000000
answer = []

while start < end:
    tmp_sum = values[start] + values[end]
    
    # 현재 합이 더 0에 가까우면 결과 갱신
    if abs(tmp_sum) < closest_sum:
        closest_sum = abs(tmp_sum)
        answer = [values[start], values[end]]
    
    # 합이 0보다 작으면 start 포인터 이동, 크면 end 포인터 이동
    if tmp_sum < 0:
        start += 1
    else:
        end -= 1

print(*answer)