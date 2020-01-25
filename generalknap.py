import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n, w = list(map(int, input().strip().split()))
    dp = [[0] * (w+5) for _ in range(n+5)]
    items = [[] for _ in range(n)]
    for i in range(n):
        items[i] = list(map(int, input().strip().split()))
    for i in range(1, n+1):
        for j in range(1, w+1):
            if j-items[i-1][1] < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-items[i-1][1]]+items[i-1][0])
    print(dp[n][w])

if __name__ == '__main__':
    main()
