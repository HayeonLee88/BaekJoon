def solution(sequence, k):
    res = []
    n = len(sequence) # start 포인터 위치 변수
    end = 0 # end 포인터
    max_sum = 0 # 연속된 부분 수열의 합
    interval = n # 연속된 부분 수열의 길이
    for start in range(n):
        while max_sum < k and end < n:
            max_sum += sequence[end]
            end += 1
        if max_sum == k and end - 1 - start < interval :
            res = [start, end - 1]
            interval = end - 1 - start # start 포인터가 커지므로 반복주기 줄이기
        max_sum -= sequence[start] # start + 1부터 더해야 하므로 빼기
    return res