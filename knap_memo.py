import sys
input = sys.stdin.readline

N = 0
W = 0
items = []
dp = []
def main():
	global N, W, items, dp
	N, W = map(int, input().strip().split())
	items = []
	for i in range(N):
		v, w = map(int, input().strip().split())
		items.append((v, w))
	dp = [[-1] * (W+1) for _ in range(N+1)]
	rec(0, W)
	print(dp[0][W])

# spaceのカバンに商品i以降を入れる時の最大値
def rec(i, space):
	if dp[i][space] != -1:
		return dp[i][space]

	if i >= N:
		dp[i][space] = 0
		return dp[i][space]

	if space - items[i][1] < 0:
		dp[i][space] = rec(i+1, space)
		return dp[i][space]

	dp[i][space] = max(
		rec(i+1, space - items[i][1]) + items[i][0],
		rec(i+1, space)
	)

	return dp[i][space]

if __name__ == '__main__':
	main()
