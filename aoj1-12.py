import sys
input = sys.stdin.readline
import heapq
INF = 10**9
WHITE = -100
GRAY = -1000
BLACK = -10000

nb = []
m = 0
color = []
d = []
p = []
q = []

def dijkstra():
	global d, nb, m, color, p, q
	d[0] = 0
	heapq.heappush(q, (0, 0))
	while len(q) != 0:
		ud, u = heapq.heappop(q)
		# print("{ud, u}", ud, u)
		color[u] = BLACK
		if d[u] < ud:
			continue
		for v, dv in nb[u]:
			if color[v] != BLACK:
				if d[u] + dv < d[v]:
					d[v] = d[u] + dv
					p[v] = u
					heapq.heappush(q, (d[v], v))


def main():
	global m, nb, color, d, p

	m = int(input().strip())
	color = [WHITE] * m
	d = [INF] * m
	p = [-1] * m
	nb = [[] for _ in range(m)]
	for i in range(m):
		l = list(map(int, input().strip().split()))
		for j in range(l[1]):
			nb[i].append((l[2 + 2 * j], l[3 + 2 * j]))
	# for i in range(m):
	# 	print(nb[i])
	dijkstra()
	for i in range(m):
		print("{} {}".format(i, d[i]))


if __name__ == '__main__':
	main()
