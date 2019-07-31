import sys
input = sys.stdin.readline
from math import sqrt

def main():
	n, D = map(int, input().strip().split())
	s = [[] for _ in range(n)]
	for i in range(n):
		s[i] = list(map(int, input().strip().split()))
	ans = 0
	for i in range(n-1):
		for j in range(i+1, n):
			d = 0
			for k in range(D):
				d += (s[i][k] - s[j][k])**2
			dist = sqrt(d)
			if int(dist) == dist:
				ans += 1
	print(ans)
if __name__ == '__main__':
	main()
