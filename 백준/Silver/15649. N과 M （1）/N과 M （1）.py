n, m = map(int, input().split())
nums = list(range(1, n + 1))
visited = [False] * (n + 1)
answer = [0] * m

def backtrack(n, m, len):
  global visited, answer
  if len == m:
    print(*answer)
    return
  else:
    for i in range(1, n + 1):
      if len < m and not visited[i]:
        answer[len] = i
        visited[i] = True
        backtrack(n, m, len + 1)
        visited[i] = False

backtrack(n, m, 0)