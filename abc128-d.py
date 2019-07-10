import sys
input = sys.stdin.readline
from collections import deque

def main():
	n, k = map(int, input().strip().split())
	v = deque(map(int, input().strip().split()))
	ans = 0
	for i in range(k+1):
		for j in range(k - i + 1):
			now = 0
			s = []
			if i + j > n:
				continue
			md = k - i - j
			for t in range(i):
				s.append(v[t])
				now += v[t]
			for t in range(j):
				s.append(v[n-1-t])
				now += v[n-1-t]
			s.sort()
			# for t in range(min(md, i+j)):
			# 	# print("t:{}, len:{}".format(t, len(s)))
			# 	if s[t] >= 0:
			# 		break
			# 	else:
			# 		s[t] = 0
			for t in range(md):
				if t >= len(s):
					break
				if s[t] >= 0:
					break
				now -= s[t]
			ans = max(now, ans)

	print(ans)


if __name__ == '__main__':
	main()
