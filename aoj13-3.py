import sys
input = sys.stdin.readline

INF = 10**9
WHITE = -100
GRAY = -1000
BLACK = -10000

def main():
	m = int(input().strip())
	s = [[-1] * m for _ in range(m)]
	for i in range(m):
		l = list(map(int, input().strip().split()))
		for j in range(l[1]):
			s[i][l[2 + 2 * j]] = l[3 + 2 * j]
	color = [WHITE] * m
	d = [INF] * m
	p = [-1] * m

	d[0] = 0
	# for i in range(m):
	# 	print(s[i])
	while True:
		mincost = INF
		for i in range(m):
			if color[i] != BLACK and d[i] < mincost:
				mincost = d[i]
				u = i
		if mincost == INF:
			break
		color[u] = BLACK
		for i in range(m):
			if color[i] != BLACK and s[u][i] != -1:
				if d[u] + s[u][i] < d[i]:
					d[i] = d[u] + s[u][i]
					p[i] = u
					# color[i] = GRAY
	for i in range(m):
		print("{} {}".format(i, d[i]))


if __name__ == '__main__':
	main()
