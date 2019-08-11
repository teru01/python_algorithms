import sys
input = sys.stdin.readline
from operator import itemgetter

def div_count(n):
	c = 0
	for i in range(1, n+1):
		if n % i == 0:
			c += 1
	return c

def main():
	n = int(input().strip())
	ans = 0
	for i in range(1, n+1):
		if i % 2 == 1 and div_count(i) == 8:
			ans += 1
	print(ans)

if __name__ == '__main__':
	main()
