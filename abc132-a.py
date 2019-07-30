import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
	s = input().strip()
	m = defaultdict(lambda : 0)
	for c in s:
		m[c] += 1
	# print(len(m))
	v = list(m.values())
	if len(m) == 2 and v[0] == 2 and v[1] == 2:
		print('Yes')
	else:
		print('No')


if __name__ == '__main__':
	main()
