import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	n, k = map(int, input().strip().split())
	# if k % 2 == 1:
	# 	print((n // k)**3)
	# else:
	# 	print((n // k)**3 + (((n-k//2)//k)+1)**3)
	for a in range(n):
		b = k - a%k
		c = k - a%k
		if (b + c) % k == 0:


if __name__ == '__main__':
	main()
