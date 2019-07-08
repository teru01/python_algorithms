import sys

x = y = z = 0
memo = []

def rec(x, y, z):
	print(x, y, z)
	if memo[x][y][z] != -1:
		# print('hit: {},{},{}'.format(x, y, z))
		return memo[x][y][z]

	if x <= y:
		memo[x][y][z] = y
		return y

	memo[x][y][z] = rec(rec(x-1, y, z), rec(y-1, z, x), rec(z-1, x, y))
	return memo[x][y][z]

# def nrec(x, y, z):
# 	print(x, y, z)
# 	if memo[x][y][z] != -1:
# 		print('hit: {},{},{}'.format(x, y, z))
# 		return memo[x][y][z]

# 	if x <= y:
# 		memo[x][y][z] = y
# 		return y

# 	memo[x][y][z] = rec(rec(x-1, y, z), rec(y-1, z, x), rec(z-1, x, y))
# 	return memo[x][y][z]

def main(argv):
	global x, y, z, memo
	x, y, z = map(int, [argv[0], argv[1], argv[2]])
	M = max([x, y, z])
	memo = [[[-1] * (M+1) for _ in range(M+1)] for _ in range(M+1)]
	print(rec(x, y, z))

if __name__ == '__main__':
	main(sys.argv[1:])
