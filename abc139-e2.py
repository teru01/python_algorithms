import sys
input = sys.stdin.readline
from operator import itemgetter

id = []
to = []
dp = []


def toid(i, j):
	if i > j:
		i, j = j, i
	return id[i][j]

def main():
	global id, to, dp
	n = int(input().strip())
	a = [0] * n
	id = [0] * n
	to = [[] for _ in range(n**2)]
	dp = [-1] * (n**2)
	for i in range(n):
		id[i] = [0] * n
		a[i] = list(map(lambda x: x-1, map(int, input().strip().split())))
	V = 0

	# 対戦に対してIDを割り振る
	for i in range(n):
		for j in range(n):
			if i < j:
				id[i][j] = V
				V += 1
	for i in range(n):
		for j in range(n-1):
			# 試合順序をIDに変換
			a[i][j] = toid(i, a[i][j])
		for j in range(n-2):
			# 試合順序グラフ作成
			to[a[i][j]].append(a[i][j+1])
	ans = 0
	for i in range(V):
		# path = [0] * n**2
		result = rec(i)
		ans = max(ans, result)
	print(ans)

def rec(i):
	global to, dp

	if dp[i] == 0:
		# print(i)
		print("-1")
		sys.exit(0)
	elif dp[i] != -1:
		return dp[i]

	dp[i] = 0
	for k in to[i]:
		dp[i] = max(dp[i], rec(k)+1)
	if len(to[i]) == 0:
		dp[i] = 1
	return dp[i]

if __name__ == '__main__':
	main()
