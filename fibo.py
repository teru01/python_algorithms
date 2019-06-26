import sys
input = sys.stdin.readline
from functools import lru_cache

# def fibo(i, dp):
# 	if dp[i] != -1:
# 		return dp[i]
# 	dp[i] = fibo(i-1, dp) + fibo(i-2, dp)
# 	return dp[i]

@lru_cache(maxsize=50)
def fibo(i):
	if i == 0 or i == 1:
		return i
	else:
		return fibo(i-1) + fibo(i-2)

def main():
	n = int(input().strip())
	dp = [-1 for i in range(n+1)]
	dp[0] = 1
	dp[1] = 1
	# print(fibo(n, dp))
	print(fibo(n))

if __name__ == '__main__':
	main()
