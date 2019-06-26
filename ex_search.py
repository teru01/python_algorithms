import sys
input = sys.stdin.readline

dp = [[-1]*20 for i in range(2000)]
def rec(v, k, i):
	if dp[k][i] != -1:
		return dp[k][i]
	if k == 0:
		dp[k][i] = 1
	elif i >= len(v):
		dp[k][i] = 0
	elif rec(v, k, i+1):
		dp[k][i+1] = 1
	elif rec(v, k-v[i], i+1):
		dp[k][i+1] = 1
	else:
		dp[k][i] = 0

	return dp[k][i]

def main():
	n = int(input().strip())
	v = list(map(int, input().strip().split()))
	m = int(input().strip())
	w = list(map(int, input().strip().split()))
	for q in w:
		if rec(v, q, 0):
			print("yes")
		else:
			print("no")

if __name__ == '__main__':
	main()
