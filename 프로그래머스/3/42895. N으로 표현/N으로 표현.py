def solution(N, number):
    dp = [{int(f"{N}" * (i + 1))} for i in range(8)]
    answer = 0
    for k in range(8):
        for i in range(k):
            for a in dp[i]:
                for b in dp[k - i - 1]:
                    dp[k].add(a + b)
                    dp[k].add(a - b)
                    dp[k].add(a * b)
                    if b != 0:
                        dp[k].add(a // b)

    for i in range(8):
        if number in dp[i]:
            return i + 1
    
    return -1