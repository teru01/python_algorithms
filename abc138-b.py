import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	n = int(input().strip())
	v = list(map(int, input().strip().split()))
	d = sum(1/x for x in v)
	print("{:.5f}".format(1/d))

if __name__ == '__main__':
	main()
