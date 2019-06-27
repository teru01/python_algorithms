import sys
input = sys.stdin.readline

N = 0
W = 0
items = []
dp = []
def main():
	global N, W, items, dp
	N, W = map(int, input().strip().split())
	for i in range(N):
		v, w = map(int, input().strip().split())
		items.append((v, w))
	#
	dp = [[-1] * (W+1) for _ in range(N+1)]
	# print('========================')
	print(val(0, W))


def val(i, space):
	global dp
	# print(i, space)
	if dp[i][space] != -1:
		return dp[i][space]

	if i > N-1:
		dp[i][space] = 0
		return dp[i][space]

	if space - items[i][1] < 0:
		dp[i][space] = val(i+1, space)
		return dp[i][space]

	dp[i][space] = max(val(i+1, space - items[i][1]) + items[i][0], val(i+1, space))
	return dp[i][space]

#dp[0][W] = 
if __name__ == '__main__':
	main()
