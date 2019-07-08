import sys
input = sys.stdin.readline
a = []
dp = []

#l <= x < rまでの行列せきの最小値
def rec(l, r):
	if dp[l][r] != -1:
		return dp[l][r]
	if l+1 == r:
		dp[l][r] = 0
		return dp[l][r]
	if l+2 == r:
		dp[l][r] = a[l][0] * a[l][1] * a[l+1][1]
		return dp[l][r]

	m = 100000000
	for i in range(l+1, r):
		m = min(m, rec(l, i) + rec(i, r) + a[l][0] * a[i][0] * a[r-1][1])
	dp[l][r] = m
	return dp[l][r]



def main():
	global a, dp
	n = int(input().strip())
	for i in range(n):
		a.append(tuple(map(int, input().strip().split())))
	dp = [[0] * (n+1) for _ in range(n+1)]

	for l in range(2, n+1):
		for i in range(1, n-l+2):
			j = i + l - 1
			m = 10000000
			for k in range(i, j):
				print(i, k, j)
				m = min(m, dp[i][k] + dp[k+1][j] + a[i][0] * a[k][0] * a[j-1][1])
			dp[i][j] = m
	print(dp[1][n])
	# print(rec(0, n))

if __name__ == '__main__':
	main()
