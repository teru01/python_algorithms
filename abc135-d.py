import sys
input = sys.stdin.readline

def main():
	mod = 10**9 + 7
	N = 13
	dp = [0] * N
	dp[0] = 1
	s = input().strip()
	mul = 1
	for i in reversed(range(len(s))):
		# print(dp)
		nextdp = [0] * N
		if s[i] == '?':
			for k in range(10):
				for j in range(N):
					# j余る数（0~Nまで）
					nextdp[(k * mul + j) % N] += dp[j]
					nextdp[(k * mul + j) % N] %= mod
		else:
			k = int(s[i])
			# print("c: {},{}".format(i, k))
			for j in range(N):
				nextdp[(k * mul + j) % N] += dp[j]
				nextdp[(k * mul + j) % N] %= mod
		mul *= 10
		mul %= N
		dp = nextdp
	# print(dp)
	print(dp[5])

if __name__ == '__main__':
	main()
