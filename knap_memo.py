import sys
input = sys.stdin.readline

N = 0
W = 0
items = []
dp = []
G = []
def main():
	global N, W, items, dp, G
	N, W = map(int, input().strip().split())
	for i in range(N):
		v, w = map(int, input().strip().split())
		items.append((v, w))
	#
	dp = [[0] * (W+1) for _ in range(N+1)]
	G = [[0] * (W+1) for _ in range(N+1)]
	# print('========================')
	# print(val(0, W))
	print(val_loop())
	# for line in G:
	# 	print(line)

	bought = []
	r, c = 0, W
	while r < N:
		print("while: {}".format(r))
		r2, c2 = G[r][c]
		if c != c2:
			bought.append(r)
		r, c = r2, c2
	for i in bought:
		print(i, end=" ")
	print('', end="\n")

def val_loop():
	# dp[N-1] = [0]*(W+1)
	global G
	for i in reversed(range(0, N)): # N-1 to 0
		for j in range(W+1):
			if j < items[i][1]:
				dp[i][j] = dp[i+1][j]
				G[i][j] = (i+1, j)
			else:
				if dp[i+1][j] < dp[i+1][j-items[i][1]] + items[i][0]:
					dp[i][j] = dp[i+1][j-items[i][1]] + items[i][0]
					G[i][j] = (i+1, j-items[i][1])
				else:
					dp[i][j] = dp[i+1][j]
					G[i][j] = (i+1, j)
	return dp[0][W] #Wの余地があるアイテムi以降を取った時

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
