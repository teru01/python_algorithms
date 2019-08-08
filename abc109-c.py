import sys
input = sys.stdin.readline
from operator import itemgetter

def gcd(a, b):
	if b % a == 0:
		return a
	else:
		return gcd(b % a, a)

def gcd_ary(ary, n):
	for i in range(n-1):
		ary[i+1] = gcd(ary[i], ary[i+1])
	return ary[n-1]

def main():
	n, x = map(int, input().strip().split())
	v = list(map(int, input().strip().split()))
	d = [0] * n
	for i in range(n):
		d[i] = abs(x - v[i])
	print(gcd_ary(d, n))

if __name__ == '__main__':
	main()
