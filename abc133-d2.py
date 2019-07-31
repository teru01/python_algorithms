import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	v = list(map(int, input().strip().split()))
	s = sum(v)
	t = sum(v[1::2])
	x = [0] * n
	# print(s, t)
	x[0] = s - 2 * t
	for i in range(1, n):
		x[i] = 2 * v[i-1] - x[i-1]
	for i in range(n):
		print("{} ".format(x[i]), end='')
	print("")


if __name__ == '__main__':
	main()
