import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	n, i = map(int, input().strip().split())
	print(n-i+1)

if __name__ == '__main__':
	main()
