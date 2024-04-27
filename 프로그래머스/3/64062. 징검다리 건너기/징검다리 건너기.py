
def solution(stones, k):
    start = 0
    end = max(stones)
    cnts = []
    while start <= end:
        mid = (start + end) // 2
        cnts = []
        tmp = 1
        for s in stones:
            if s <= mid:
                tmp += 1
            else:
                cnts.append(tmp)
                tmp = 1
        cnts.append(tmp)

        if max(cnts) > k:
            end = mid - 1
        else:
            start = mid + 1
            
    if max(cnts) <= k:
        return mid + 1
    return mid