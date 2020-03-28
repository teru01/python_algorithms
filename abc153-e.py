import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 1000000

def main():
    h, n = list(map(int, input().strip().split()))
    a = [0] * (n+1)
    b = [0] * (n+1)
    for i in range(1, n+1):
        a[i], b[i] = list(map(int, input().strip().split()))
    dp = [[INF] * (h+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(n):
        for j in range(h+1):
            nj = min(h, j+a[i])
            dp[i][nj] = min(dp[i][nj], dp[i+1][j] + b[i])
            # if j-a[i] < 0:
            #     dp[i][j] = dp[i-1][j]
            # else:
            #     dp[i][j] = min(dp[i-1][j], dp[i][j-a[i]] + b[i])
    print(dp[n][h])
    # for i in range(n+1):
    #     for j in range(h+10):
    #         print("{} ".format(dp[i][j]), end='')
    #     print('')
if __name__ == '__main__':
    main()
