import sys
input = sys.stdin.readline
from collections import deque

def main():
	n = int(input().strip())
	v = [[] for _ in range(n)]
	for i in range(n):
		v[i] = list(map(int, input().strip().split()))
	l = [-1] * (n+1)
	q = deque()
	q.append((1, 0))
	while len(q) != 0:
		id, d = q.popleft()
		if l[id] != -1:
			continue
		l[id] = d
		for i in range(v[id-1][1]):
			q.append((v[id-1][2+i], d+1))
	for i in range(1, n+1):
		print(i, l[i])

if __name__ == '__main__':
	main()
