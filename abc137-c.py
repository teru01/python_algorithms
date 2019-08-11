import sys
input = sys.stdin.readline
from operator import itemgetter
from collections import defaultdict

def main():
	n = int(input().strip())
	st = defaultdict(int)
	for i in range(n):
		s = input().strip()
		d = []
		for c in s:
			d.append(ord(c))
		d.sort()
		st[tuple(d)] += 1
	ans = 0
	for v in st.values():
		if v == 1:
			continue
		ans += v*(v-1) // 2
	print(ans)

if __name__ == '__main__':
	main()
