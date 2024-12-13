import sys


input = lambda:sys.stdin.readline().rstrip()

start, end, quit = input().split()

start = list(map(int, start.split(':')))
end = list(map(int, end.split(':')))
quit = list(map(int, quit.split(':')))

members = dict()

attend = set()
leave = set()

answer = 0
while True:
    try:
        time, nickname = input().split()
    except:
        break

    time = list(map(int, time.split(':')))

    if time[0] < start[0] or (time[0] == start[0] and time[1] <= start[1]):
        members[nickname] = []
    
    if (end[0] < time[0] or (time[0] == end[0] and end[1] <= time[1])) and(time[0] < quit[0] or (time[0] == quit[0] and time[1] <= quit[1])):
        try:
            del members[nickname]
            answer += 1
        except:
            pass

print(answer)