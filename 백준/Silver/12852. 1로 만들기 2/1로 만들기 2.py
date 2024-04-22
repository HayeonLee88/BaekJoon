n = int(input())
cnt = [0] * (n + 1) # 1이 만들어기지 위한 최소 횟수를 담는 리스트
prev = [0] * (n + 1) # 이전의 숫자를 담는 리스트
for i in range(2, n + 1):
    cnt[i] = cnt[i - 1] + 1 # 이전의 수에서 1을 더하는 경우
    prev[i] = i - 1
    if i % 2 == 0 and cnt[i] > cnt[i // 2] + 1: # 2의 배수인 경우
        cnt[i] = cnt[i // 2] + 1
        prev[i] = i // 2
    if i % 3 == 0 and cnt[i] > cnt[i // 3] + 1: # 3의 배수인 경우
        cnt[i] = cnt[i // 3] + 1
        prev[i] = i // 3

print(cnt[n])
while n > 0:
    print(n, end=" ")
    n = prev[n]