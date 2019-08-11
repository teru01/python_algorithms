import sys
input = sys.stdin.readline
from operator import itemgetter
import heapq

def main():
	n, m = map(int, input().strip().split())
	ab = [0] * n
	for i in range(n):
		ab[i] = list(map(int, input().strip().split()))
	ab.sort(key=itemgetter(1), reverse=True)
	ab.sort(key=itemgetter(0))
	hp = []
	w = 0
	t = ab[0][0]
	ans = 0
	while t <= m:
		while w < len(ab) and ab[w][0] == t:
			heapq.heappush(hp, -ab[w][1])
			w += 1
		if len(hp) > 0:
			ans += -heapq.heappop(hp)
		t += 1
	print(ans)


if __name__ == '__main__':
	main()
