'''
5:54 ~ 6:05
stack, 우선순위 큐?
'''
import heapq
def time2minute(time):
    result = 0
    hour = time[:2]
    minute = time[3:]
    result += int(hour) * 60 + int(minute)
    return result

def solution(book_time):
    answer = 1
    h = []
    book_time2minute = [[time2minute(s), time2minute(e)] for s, e in book_time]
    book_time2minute.sort()
    end = -10
    heapq.heappush(h, (book_time2minute[0][1] + 10))
    for start, end in book_time2minute[1:]:
        prev_end = heapq.heappop(h)
        if prev_end > start:
            heapq.heappush(h, (prev_end))
            heapq.heappush(h, (end + 10))
            answer = max(answer, len(h))
        else:
            heapq.heappush(h, (end + 10))
            
    return answer