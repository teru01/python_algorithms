import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	v = list(map(int, input().strip().split()))
	w = sorted(v)
	c = 0
	for i in range(n):
		if v[i] != w[i]:
			c += 1
	if c == 0 or c == 2:
		print('YES')
	else:
		print('NO')

if __name__ == '__main__':
	main()
