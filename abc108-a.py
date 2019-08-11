import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	n = int(input().strip())
	print((n // 2) * ((n+1) // 2))

if __name__ == '__main__':
	main()
