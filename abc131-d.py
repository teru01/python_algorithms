import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	n = int(input().strip())
	s = [[0] * 2 for _ in range(n)]
	for i in range(n):
		s[i][0], s[i][1] = map(int, input().strip().split())
	s2 = sorted(s, key=itemgetter(1))
	t = 0
	for item in s2:
		t += item[0]
		if t > item[1]:
			print('No')
			return
	print('Yes')

if __name__ == '__main__':
	main()
