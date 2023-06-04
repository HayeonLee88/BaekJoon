# 11052번: 카드 구매하기
# DP
n = int(input())

if n > 1:
    cards_cost = list(map(int, input().split()))
    answer = [0]

    for i in range(1, n + 1):
        answer.append(cards_cost[i-1])
        for j in range(1, i + 1):
            answer[i] = max(answer[i], answer[i-j] + answer[j])

    print(answer[-1])
else:
    print(input())
