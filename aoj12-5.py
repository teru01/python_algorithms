import sys
input = sys.stdin.readline
from collections import deque

def main():
	n, m = map(int, input().strip().split())
	g = [[] for _ in range(n)]
	cl = [-1] * n
	for i in range(m):
		s, t = map(int, input().strip().split())
		g[s].append(t)
		g[t].append(s)

	q = deque()
	color = 0
	for i in range(n):
		if cl[i] != -1:
			# すでに色がついているもの
			continue
		q.append(i)
		while len(q) != 0:
			node = q.popleft()
			# ノードに色をつける
			cl[node] = color
			for e in g[node]:
				if cl[e] != -1:
					# すでに訪問済み
					continue
				else:
					# 隣接ノードをキューに追加
					q.append(e)
		color += 1
	l = int(input().strip())
	for i in range(l):
		s, t = map(int, input().strip().split())
		if cl[s] == cl[t]:
			print('yes')
		else:
			print('no')


if __name__ == '__main__':
	main()
