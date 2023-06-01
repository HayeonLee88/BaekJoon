# 3020 개똥벌레
# 누적합을 사용하여 반복 횟수를 줄인다
import sys
input = lambda :sys.stdin.readline().rstrip()
n, h = map(int, input().split())
bottom = [0] * (h + 1)
top = [0] * (h + 1)
result = []
for i in range(n):
    k = int(input())
    if i % 2 == 0:
        # 석순
        bottom[k] += 1
    else: # 종유석
        top[h - k + 1] +=1
for i in range(3, h + 1):
    top[i] += top[i - 1]
    bottom[h + 1 - i] += bottom[h + 2 - i]
m = 200001
cnt = 0
for i in range(1, h + 1):
    tmp = top[i] + bottom[i]
    result.append(tmp)
    if m > tmp:
        cnt = 1
        m = tmp
    elif m == tmp:
        cnt += 1
print(m, cnt)