import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from itertools import combinations

def distance(i, j):
	return min(abs(j - i), abs(24-j+i))

def main():
	n = int(input().strip())
	v = sorted(list(map(int, input().strip().split())))
	t = [0] * 24
	for i in range(n):
		if t[v[i]] == 1:
			t[24 - v[i]] += 1
		t[v[i]] = i

if __name__ == '__main__':
	main()
