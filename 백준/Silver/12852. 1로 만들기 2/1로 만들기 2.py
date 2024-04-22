n = int(input())
cnt_n_prev = [[0, 0] for i in range(n + 1)] # 1이 만들어기지 위한 횟수와 이전의 숫자를 담는 리스트

for i in range(2, n + 1):
    cnt_n_prev[i][0] = cnt_n_prev[i - 1][0] + 1 # 이전의 수에서 1을 더하는 경우
    cnt_n_prev[i][1] = i - 1
    if i % 2 == 0 and cnt_n_prev[i][0] > cnt_n_prev[i // 2][0] + 1: # 2의 배수인 경우
        cnt_n_prev[i][0] = cnt_n_prev[i // 2][0] + 1
        cnt_n_prev[i][1] = i // 2
    if i % 3 == 0 and cnt_n_prev[i][0] > cnt_n_prev[i // 3][0] + 1: # 3의 배수인 경우
        cnt_n_prev[i][0] = cnt_n_prev[i // 3][0] + 1
        cnt_n_prev[i][1] = i // 3
        
print(cnt_n_prev[n][0])
print(n, end=' ')
while cnt_n_prev[n][1] != 0:
    print(cnt_n_prev[n][1], end=' ')
    n = cnt_n_prev[n][1]
