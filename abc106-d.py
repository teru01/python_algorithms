import sys
input = sys.stdin.readline
from operator import itemgetter

c = []

def main():
	global c
	n, m, q = map(int, input().strip().split())
	xy = [[0] * (n+1) for _ in range(n+1)]
	for i in range(m):
		l, r = map(int, input().strip().split())
		xy[l][r] += 1
	c = [[0] * (n+2) for _ in range(n+1)]
	for i in range(n+1):
		for j in range(n+1):
			c[i][j+1] = xy[i][j] + c[i][j]

	# print(c)
	for i in range(q):
		ans = 0
		p, q = map(int, input().strip().split())
		for k in range(p, q+1):
			ans += c[k][q+1] - c[k][p]
		print(ans)

if __name__ == '__main__':
	main()
