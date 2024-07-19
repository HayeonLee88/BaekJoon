from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    
    while True:
        answer += 1
        if len(people) > 1:
            if people[0] + people[-1] <= limit:
                people.popleft()
            people.pop()
        else:
            break
            
    if not people:
        answer -= 1
        
    return answer