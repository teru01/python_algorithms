import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n, m = list(map(int, input().strip().split()))
    c = list(map(int, input().strip().split()))
    dp = [[0] * (n+5) for _ in range(m+5)]
    dp[0] = [INF] * (n+5)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if j - c[i-1] < 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]+1)
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-c[i-1]]+1)
    print(dp[m][n])


if __name__ == '__main__':
    main()
