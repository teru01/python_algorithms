import sys
input = sys.stdin.readline
from math import sqrt
from bisect import bisect_right

def main():
	n, m = map(int, input().strip().split())
	M = int(sqrt(m))
	ans = 1
	for i in range(1, M+1):
		if m % i == 0:
			if i*n <= m:
				ans = max(ans, i)
			if m//i * n <= m:
				ans = max(ans, m//i)
	print(ans)

if __name__ == '__main__':
	main()
