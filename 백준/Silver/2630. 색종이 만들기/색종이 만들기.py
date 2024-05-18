import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
color_dict = {0:0, 1:0}

def search(n, x, y):
	global graph
	color = graph[x][y]

	for i in range(x, x + n):
		for j in range(y, y + n):
			if graph[i][j] != color:
				n //= 2
				search(n, x, y)
				search(n, x, y + n)
				search(n, x + n, y)
				search(n, x + n, y + n)
				return 
	color_dict[color] += 1

search(n, 0, 0)
print(*color_dict.values(), sep='\n')
