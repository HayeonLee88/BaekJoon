# 14469번: 소가 길을 건너간 이유 3
n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x:x[0])
answer = 0
for x in data:
  answer = max(answer, x[0]) + x[1]
print(answer)