import sys
input = sys.stdin.readline

v = []
n = 0
k = 0
memo = []
memo2 = []

def rec(i, j):
	global v, n, k, memo, memo2
	if memo[i][j] != -1:
		return memo[i][j]
	if i == j:
		if v[i] >= k:
			memo[i][j] = 1
		else:
			memo[i][j] = 0
		return memo[i][j]
	c = 0
	if memo2[j+1]-memo2[i] >= k:
		c = 1
	if i+1 == j:
		memo[i][j] = c + rec(i+1, j) + rec(i, j-1)
		return memo[i][j]
	memo[i][j] = c + rec(i+1, j) + rec(i, j-1) - rec(i+1, j-1)
	return memo[i][j]

def main():
	global n, k, v, memo, memo2
	n, k = map(int, (input().strip().split()))
	v = list(map(int, input().strip().split()))
	memo = [[0] * n for _ in range(n)]
	memo2 = [0] * (n+1)
	p = 0
	for i in range(1, n+1):
		memo2[i] = memo2[i-1] + v[i-1]
	# 二乗オーダー、累積和がO(1)でもとまるので漸化式にする必要もない
	for l in range(n+1):
		for i in range(n-l):
			j = i + l

			if i == j:
				if v[i] >= k:
					memo[i][j] = 1
				else:
					memo[i][j] = 0
				continue
			c = 0
			if memo2[j+1] - memo2[i] >= k:
				c = 1
				# print(i, j)
				p += 1
			if i+1 == j:
				memo[i][j] = c + memo[i][j-1] + memo[i+1][j]
				continue
			memo[i][j] = c + memo[i][j-1] + memo[i+1][j] - memo[i+1][j-1]
	print(memo[0][n-1])
	
	# print(p)
	
	
	# print(rec(0, n-1))

if __name__ == '__main__':
	main()
