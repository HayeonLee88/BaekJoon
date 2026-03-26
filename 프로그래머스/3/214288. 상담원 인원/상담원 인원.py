import heapq

def solution(k, n, reqs):
    answer = 0
    reqs_type = {num: [] for num in range(1, k + 1)}
    reqs.sort(key=lambda x: (x[2], x[0]))
    reqs_type[reqs[0][2]].append((reqs[0][0], reqs[0][1]))
    
    for i, (a, b, c) in enumerate(reqs[1:]):
        reqs_type[c].append((a, b))
    
    max_mentor = n - k + 1
    wait = [[0] * (max_mentor + 1) for _ in range(k + 1)]
    for num in range(1, k + 1):
        max_ = n - (k - 1)
        for i in range(1, max_ + 1):
            waiting = 0
            h = []
            if reqs_type[num][0:1]:
                a, b = reqs_type[num][0]
                heapq.heappush(h, (a + b, a))
            prev_end, prev_start = 0, 0
            for start, time in reqs_type[num][1:]:
                while h:
                    prev_end, prev_start = heapq.heappop(h)
                    if prev_end > start:
                        heapq.heappush(h, (prev_end, prev_start))
                        break
                if len(h) == i:
                    prev_end, prev_start = heapq.heappop(h)
                    waiting += prev_end - start
                    heapq.heappush(h, (prev_end + time, prev_end))
                else:
                    heapq.heappush(h, (start + time, start))
            wait[num][i] = waiting
    
    INF = float('inf')
    dp = [[INF] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 0

    for c in range(1, k + 1):
        for used in range(c, n + 1):
            for m in range(1, used - (c - 1) + 1):
                if m <= max_mentor:
                    dp[c][used] = min(dp[c][used], dp[c - 1][used - m] + wait[c][m])

    return dp[k][n]
