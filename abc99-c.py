import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    n = int(input().strip())
    dp = [0] * (n+1)
    # coins = [0] + [6**i for i in range(8)] + [9 ** i for i in range(1, 7)]
    for i in range(1, n+1):
        dp[i] = 10**10

    for b in (6, 9):
        p = 0
        while b**p <= n:
            for i in range(n+1):
                if b**p <= i:
                    dp[i] = min(dp[i], dp[i-b**p]+1)
            p += 1
    print(dp[n])
if __name__ == '__main__':
    main()
