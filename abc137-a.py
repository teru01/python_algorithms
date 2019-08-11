import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	a, b = map(int, input().strip().split())
	print(max(a+b, a-b, a*b))

if __name__ == '__main__':
	main()
