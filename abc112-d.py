import sys
input = sys.stdin.readline
from math import sqrt
from bisect import bisect_right

def main():
	n, m = map(int, input().strip().split())
	M = int(sqrt(m))
	l = []
	for i in range(1, M+1):
		if m % i == 0:
			l.append(i)
			l.append(m // i)
	l.sort()
	k = m//n
	ind = bisect_right(l, k)
	# print(l)
	print(l[ind-1])

if __name__ == '__main__':
	main()
