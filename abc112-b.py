import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	n, T = map(int, input().strip().split())
	s = [0] * n
	ans = 10**9
	for i in range(n):
		c, t = map(int, input().strip().split())
		if t <= T and c < ans:
			ans = c
	if ans == 10**9:
		print('TLE')
	else:
		print(ans)

if __name__ == '__main__':
	main()
