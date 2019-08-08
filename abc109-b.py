import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	n = int(input().strip())
	v = [0] * n
	for i in range(n):
		v[i] = input().strip()
	if len(set(v)) != n:
		print('No')
		return
	for i in range(n-1):
		if v[i][-1] != v[i+1][0]:
			print('No')
			return
	print('Yes')

if __name__ == '__main__':
	main()
