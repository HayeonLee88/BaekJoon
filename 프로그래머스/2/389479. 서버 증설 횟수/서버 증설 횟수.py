'''
server = [증설 시간]
total = 서버 이용 가능 최대 사람수
'''
from collections import deque

def solution(players, m, k):
    answer = 0
    time = 0
    server = deque()
    len_ = len(server)
    while time < 24:
        len_ = len(server)
        player = players[time]
        if len_ < player // m:
            cnt = player // m - len_
            answer += cnt
            for _ in range(cnt):
                server.append(time)
        time += 1
        if server and server[0] + k == time:
            len_ = len(server)
            for _ in range(len_):
                now = server.popleft()
                if now + k == time:
                    continue
                server.appendleft(now)
                break
            len_ = len(server)
    return answer