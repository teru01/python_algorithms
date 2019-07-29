import sys
input = sys.stdin.readline

INF = 10**9
WHITE = -100
GRAY = -1000
BLACK = -10000

def main():
	m = int(input().strip())
	s = [[] for _ in range(m)]
	for i in range(m):
		s[i] = list(map(int, input().strip().split()))
	d = [INF] * m
	color = [WHITE] * m
	p = [-1] * m
	d[0] = 0
	u = None
	while True:
		mincost = INF
		for i in range(m):
			if color[i] != BLACK and d[i] < mincost:
				mincost = d[i]
				u = i
		
		if mincost == INF:
			break
		
		color[u] = BLACK

		for v in range(m):
			if color[v] != BLACK and s[u][v] != -1:
				if s[u][v] < d[v]:
					d[v] = s[u][v]
					p[v] = u
					color[v] = GRAY
	ans = 0
	for i in range(1, m):
		ans += s[i][p[i]]
	print(ans)


if __name__ == '__main__':
	main()
