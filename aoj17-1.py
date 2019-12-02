import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n, m = list(map(int, input().strip().split()))
    c = [0] + list(map(int, input().strip().split()))
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(n+1):
        dp[0][i] = INF
    for i in range(1, m+1):
        for j in range(1, n+1):
            if j - c[i] < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-c[i]] + 1)
    print(dp[m][n])

if __name__ == '__main__':
    main()
