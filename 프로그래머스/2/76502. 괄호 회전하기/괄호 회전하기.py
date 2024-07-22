def solution(s):
    answer = 0
    stack = []
    n = len(s)
    
    dic = {'(': ')', '[': ']', '{': '}'}
    if n % 2 != 0:
        return 0
    
    for _ in range(n):
        check = True
        for x in s:
            if x in ['(', '[', '{']: # 열림 괄호라면
                stack.append(x)
            else:
                if stack: 
                    prev = stack.pop()
                    if dic[prev] != x: # 최근 열림 괄호와 현재 닫힘 괄호의 모양이 다를 때
                        check = False
                        break
                else: # 열림 괄호와 닫힘 괄호의 개수가 안 맞을 때
                    check = False
                    break
        if check:
            answer += 1
        s = s[1:] + s[0]
                

    return answer