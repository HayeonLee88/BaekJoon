'''
1:28~
diff ≤ level: time_cur
diff > level: (diff - level) * (time_cur + time_prev)
- (diff - level)번 이후: time_cur
limit: 퍼즐을 모두 해결하기 위한 제한시간
제한시간 내에 풀 수 있는 숙련되의 최솟값.
이진탐색: 가장 큰 diff값 = end
'''
def solution(diffs, times, limit):
    mid = 0
    total = 0
    start = 1
    end = max(diffs)
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i, diff in enumerate(diffs):
            if diff <= mid:
                total += times[i]
            else:
                if i == 0:
                    total += (diff - mid + 1) * times[i]
                else:
                    total += (diff - mid) * (times[i] + times[i - 1]) + times[i]
            if total > limit:
                break
        if total <= limit:
            end = mid - 1
            answer = mid
        elif total > limit:
            start = mid + 1
    return start