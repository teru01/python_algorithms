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
	t = [0] * n

	for i in range(n):
		d = v[i]
		if i % 2 == 0:
			t[i] = d
		else:
			t[i] = 24 - d
	cmin = min(v) #chokudaiとの時差
	for z in combinations(range(n), 2):
		i, j = z[0], z[1]
		cmin = min(cmin, distance(t[i], t[j]))
	print(cmin)

if __name__ == '__main__':
	main()
