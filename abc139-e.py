import sys
input = sys.stdin.readline
from operator import itemgetter
from collections import deque

def main():
	n = int(input().strip())
	dqlist = [0] * (n+1)
	for i in range(n):
		v = list(map(int, input().strip().split()))
		dqlist[i+1] = deque(v)
	day = 0
	zeroc = 0
	for _ in range(1000000):
		picked = [0] * (n+1)
		changed = False
		for i in range(1, n+1):
			if picked[i] == 1:
				continue
			if len(dqlist[i]) == 0:
				continue
			if dqlist[dqlist[i][0]][0] == i:
				if picked[dqlist[i][0]] == 1:
					continue
				# OK
				changed = True
				c = dqlist[i].popleft()
				dqlist[c].popleft()
				picked[i] = 1
				picked[c] = 1
				if len(dqlist[i]) == 0:
					zeroc += 1
				if len(dqlist[c]) == 0:
					zeroc += 1
		if changed == False:
			if zeroc == n:
				print(day)
				return
			else:
				print(-1)
				return
		day += 1

if __name__ == '__main__':
	main()
