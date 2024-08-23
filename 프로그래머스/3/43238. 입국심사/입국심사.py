def solution(n, times):
    times.sort()
    start = 1
    end = times[-1] * n
    answer = end + 1
    
    while start <= end:
        mid = (start + end) // 2
        tmp = 0
        for time in times:
            tmp += (mid // time)
            if tmp >= n:
                answer = min(answer, mid)
                break
        if tmp < n:
            start = mid + 1
        elif tmp >= n:
            end = mid - 1
    return answer