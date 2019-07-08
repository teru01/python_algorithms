import sys

x = y = 0
memo = []

def rec(x, y):
	# print(x, y)
	if memo[x][y] != -1:
		print('hit: {},{}'.format(x, y))
		return memo[x][y]

	if x <= y:
		memo[x][y] = y
		return y

	memo[x][y] = rec(rec(x-1, y), rec(y-1, x))
	return memo[x][y]

def main(argv):
	global x, y, memo
	x, y = map(int, [argv[0], argv[1]])
	M = max([x, y])
	memo = [[-1] * (M+1) for _ in range(M+1)]
	print(rec(x, y))

if __name__ == '__main__':
	main(sys.argv[1:])
