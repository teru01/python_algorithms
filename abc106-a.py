import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	a, b = map(int, input().strip().split())
	print((a-1)*(b-1))

if __name__ == '__main__':
	main()
