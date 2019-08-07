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

def dfs(elm):
	global M, v, e, ans, color
	color[elm] = BLACK
	for i in M[elm]:
		if color[i] == WHITE:
			dfs(i)
	ans.appendleft(elm)

def main():
	global M, v, e, ans, color
	v, e = map(int, input().strip().split())
	M = [[] for _ in range(v)]
	for _ in range(e):
		s, t = map(int, input().strip().split())
		M[s].append(t)
	color = [WHITE] * v
	for i in range(v):
		if color[i] == WHITE:
			dfs(i)
	for i in range(v):
		e = ans.popleft()
		print(e)

if __name__ == '__main__':
	main()
