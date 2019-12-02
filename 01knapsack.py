import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n, W = list(map(int, input().strip().split()))
    items = [[0, 0] for _ in range(n+1)]
    for i in range(1, n+1):
        items[i][0], items[i][1] = list(map(int, input().strip().split()))
    dp = [[0] * (W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            if j - items[i][1] < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-items[i][1]]+items[i][0], dp[i-1][j])
    print(dp[n][W])

if __name__ == '__main__':
    main()
