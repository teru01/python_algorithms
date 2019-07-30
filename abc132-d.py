import sys
input = sys.stdin.readline
from math import factorial
c = [[0]*2001 for _ in range(2001)]
def init():
	global c
	c[0][0] = 1
	for i in range(2000):
		for j in range(i+1):
			c[i+1][j] += c[i][j]
			c[i+1][j+1] += c[i][j]
def main():
	n, k = map(int, input().strip().split())
	global c
	init()
	for i in range(1, k+1):
		if i-1 > n - k:
			print(0)
			continue
		
		# c = factorial(k-1)//(factorial(k-i)*factorial(i-1))
		# noko = factorial(n-k+1)//(factorial(i) * factorial(n-k-i+1))
		# print(c, noko)
		ans = c[k-1][i-1] * c[n-k+1][i]
		# print(ans)
		ans %= 10**9+7
		print(ans)


if __name__ == '__main__':
	main()
