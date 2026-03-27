'''
9:45 ~

'''
import heapq

def solution(k, n, reqs):
    answer= 0
    req_info = {num: [] for num in range(1, k + 1)}
    for a, b, c in reqs:
        req_info[c].append((a, b))
    
    max_cnt = n - k + 1
    waiting = [[0] * (max_cnt + 1) for _ in range(k + 1)]
    for num in range(1, k + 1):
        for i in range(1, max_cnt + 1):
            h = []
            wait = 0
            if req_info[num]:
                s, t = req_info[num][0]
                e = s + t
                heapq.heappush(h, (e, s))
            for start, time in req_info[num][1:]:
                while h:
                    prev_end, prev_start = heapq.heappop(h)
                    # 아직 끝나지 않음
                    if prev_end > start:
                        heapq.heappush(h, (prev_end, prev_start))
                        break
                # 기다릴 때
                if len(h) == i:
                    prev_end, prev_start = heapq.heappop(h)
                    wait += prev_end - start
                    heapq.heappush(h, (prev_end + time, prev_end))
                # 기다리지 않을 때
                else:
                    heapq.heappush(h, (start + time, start))
            waiting[num][i] = wait
    
    INF = int(1e9)
    # dp[i][j]: i번 상담사를 j명 썼을 때 총 기다림 시간
    dp =  [[INF] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 0
    
    for num in range(1, k + 1):
        for used in range(num, n + 1):
            for i in range(1, used - (num - 1) + 1):
                if i <= max_cnt:
                    dp[num][used] = min(dp[num][used], dp[num - 1][used - i] + waiting[num][i])
    answer = dp[k][n]
    return answer