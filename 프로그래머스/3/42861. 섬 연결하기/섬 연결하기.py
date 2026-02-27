'''
11:37~42
'''
def solution(n, costs):
    answer = 0
    parents = list(range(n))
    costs.sort(key=lambda x: x[2])
    
    def find(x):
        if parents[x] == x:
            return x
        parents[x] = find(parents[x])
        return parents[x]
    
    def union(a, b):
        a, b = find(a), find(b)
        if a < b:
            parents[b] = a
        elif a > b:
            parents[a] = b
        else:
            return True
        return False
    
    n -= 1
    for a, b, cost in costs:
        if not union(a, b):
            answer += cost
            n -= 1
            if n == 0:
                break

    return answer