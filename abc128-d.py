import sys
input = sys.stdin.readline
from collections import deque

def main():
	n, k = map(int, input().strip().split())
	v = deque(map(int, input().strip().split()))
	if v[0] > 0 and v[n-1] > 0:
		

if __name__ == '__main__':
	main()
