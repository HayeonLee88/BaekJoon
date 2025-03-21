'''
5:25~
n: 총 논문 편수
h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용 됐을 때 h의 최댓값을 구하라
h <= n
5편
3 0 6 1 5
정렬 -> 6 5 1 3 0

'''
def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse=True)
    for i in range(n, 0, -1):
        if citations[i - 1] < i:
            continue
        answer = i
        break
    return answer