import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	n = int(input().strip())
	v = list(map(int, input().strip().split()))
	v.sort()
	ans = v[0]
	for i in range(1, n):
		ans = (ans+v[i])/2
	print("{:.5f}".format(ans))


if __name__ == '__main__':
	main()
