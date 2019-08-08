import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	a, b = map(int, input().strip().split())
	for i in range(1, 4):
		if a * b * i % 2 == 1:
			print('Yes')
			return
	print('No')

if __name__ == '__main__':
	main()
