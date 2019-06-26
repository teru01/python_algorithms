import sys
input = sys.stdin.readline

def main():
	N, W = map(int, input().strip().split())
	items = [(-100, -100)]
	for i in range(N):
		v, w = map(int, input().strip().split())
		items.append((v, w))
	dp = [[0] * (W+1) for i in range(N+1)]
	for i in range(1, N+1):
		for j in range(1, W+1):
			# if dp[i][j-1] + items[1]
			if items[i][1] <= j and dp[i-1][j-items[i][1]] + items[i][0] > dp[i-1][j]:
				dp[i][j] = dp[i-1][j-items[i][1]] + items[i][0]
			else:
				dp[i][j] = dp[i-1][j]
	print(dp[N][W])

if __name__ == '__main__':
	main()
