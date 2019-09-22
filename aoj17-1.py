import sys
input = sys.stdin.readline
from operator import itemgetter

dp = []

def main():
	global dp
	n, m = list(map(int, input().strip().split()))
	v = list(map(int, input().strip().split()))
	dp = [[0] * (n+1) for _ in range(m+1)]
	dp[0] = [10**9] * (n+1)
	for i in range(1, m+1):
		for j in range(1, n+1):
			if j - v[i-1] >= 0:
				dp[i][j] = min(dp[i-1][j], dp[i][j-v[i-1]]+1)
			else:
				dp[i][j] = dp[i-1][j]
			# k = dp[i-1][j]
			# l = dp[i][j-v[i-1]]+1
			# print(dp[i][j], end=" ")
		# print("")
	print(dp[m][n])

if __name__ == '__main__':
	main()
