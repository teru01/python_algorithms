import sys
input = sys.stdin.readline
from collections import deque

M = []
v = 0
e = 0
ans = deque()
color = []
WHITE = -10
BLACK = 234
indeg = []

def bfs(elm):
	global M, v, e, ans, color, indeg
	q = deque()
	q.appendleft(elm)
	while len(q) != 0:
		u = q.pop()
		color[u] = BLACK
		ans.append(u)
		for v in M[u]:
			indeg[v] -= 1
			if indeg[v] == 0 and color[v] == WHITE:
				q.appendleft(v)

def main():
	global M, v, e, ans, color, indeg
	v, e = map(int, input().strip().split())
	M = [[] for _ in range(v)]
	for _ in range(e):
		s, t = map(int, input().strip().split())
		M[s].append(t)
	color = [WHITE] * v

	indeg = [0] * v
	for i in range(v):
		for elm in M[i]:
			indeg[elm] += 1
	for i in range(v):
		if color[i] == WHITE and indeg[i] == 0:
			bfs(i)
	for i in ans:
		print(i)

if __name__ == '__main__':
	main()
