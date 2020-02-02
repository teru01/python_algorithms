import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    h, w = list(map(int, input().strip().split()))
    c = [[0] * w for _ in range(h)]
    dp = [[0] * (w+1) for _ in range(h+1)]
    for i in range(h):
        c[i] = list(map(int, input().strip().split()))
    ans = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == 1:
                dp[i+1][j+1] = 0
            else:
                dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1
                ans = max(ans, dp[i+1][j+1])
    print(ans ** 2)
    # for i in dp:
    #     print(i)

if __name__ == '__main__':
    main()
