n, k  = map(int, input().split())
data = list(map(int, input().split()))
hap = sum(data[:k])
answer = hap
for i in range(1, n-k+1):
    hap = hap + data[i+k-1] - data[i-1]
    answer = max(answer, hap)
print(answer)