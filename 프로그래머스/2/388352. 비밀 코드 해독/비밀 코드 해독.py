from itertools import combinations

def solution(n, q, ans):
    codes = list(combinations(range(1, n + 1), 5))
    answer = len(codes)
    m = len(ans)
    for code in codes:
        code = list(code)
        for i in range(m):
            tmp = 0
            ans[i]
            for j in range(5):
                if q[i][j] in code:
                    tmp += 1
            if ans[i] != tmp:
                answer -= 1
                break
                
    return answer