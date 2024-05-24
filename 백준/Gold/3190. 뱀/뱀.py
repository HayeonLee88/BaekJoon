from collections import deque

n = int(input()) # 보드의 크기
graph = [[0] * (n + 1) for _ in range(n + 1)]

k = int(input()) # 사과의 개수
for i in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1 # 사과는 1

l = int(input()) # 방향 전환 횟수: x초 뒤, L은 왼쪽, D는 오른쪽으로 90도 회전
info = [(input().split()) for _ in range(l)]

# 이동 방향을 담는 변수
# +1 왼쪽 회전, -1 오른쪽 회전
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
i, index = 0, 0 # i: 회전 방향, index: 회전 정보 인덱스

# 회전 함수: +1 왼쪽 회전, -1 오른쪽 회전
def rotate(c):
  global i
  if c == 'L':
    i = (i + 1) % 4
  else:
    i = (i - 1) % 4

# 뱀의 몸의 위치를 저장할 덱
snake = deque()
snake.append([1,1])
time = 0
x, y = 1, 1 # 뱀의 현재 머리 위치
graph[x][y] = 2 # 뱀이 있는 곳은 2
while True:
    # 이동한 머리의 위치
    nx, ny = x + dx[i], y + dy[i]
    # 벽에 부딪히거나 자신의 몸에 닿았을 때
    if nx <= 0 or nx > n or ny <= 0 or ny > n or graph[nx][ny] == 2:
        time += 1 # 1초를 더한 후 종료
        break
    # 뱀의 머리 위치에 사과가 없다면 꼬리 꺼내기
    if graph[nx][ny] == 0:
        px, py = snake.popleft()
        graph[px][py] = 0
    # 뱀의 머리가 있는 칸을 2로 수정, 뱀 머리 칸 덱에 추가
    graph[nx][ny] = 2  
    snake.append([nx, ny])
    x, y = nx, ny # 뱀의 머리 위치 수정
    time += 1
    # 방향 정보의 시간과 현재 시간이 일치할 때
    if index < l and time == int(info[index][0]):
        rotate(info[index][1])
        index += 1
print(time)   