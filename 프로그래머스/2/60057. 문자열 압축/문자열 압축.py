def solution(s):
    length = len(s)
    answer = length
    
    def compression(n):
        prev = ''
        now = ''
        cnt = 1
        compressed = 0
        
        for i in range(0, length, n):
            now = s[i: i + n]
            if prev == s[i: i + n]:
                cnt += 1
            else:
                if cnt > 1:
                    compressed += len(str(cnt))
                compressed += len(prev)
                cnt = 1  
            prev = now
            
        if cnt > 1:
            compressed += len(str(cnt))
        compressed += len(prev)
        
        return compressed
    
    for i in range(1, length // 2 + 1):
        answer = min(answer, compression(i))
        
    return answer