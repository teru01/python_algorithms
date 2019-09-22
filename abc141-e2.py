import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
    n = int(input().strip())
    v = input().strip()
    ans = 0
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in reversed(range(n)):
        for j in reversed(range(n)):
            if v[i] == v[j]:
                dp[i][j] = dp[i+1][j+1] + 1
                ans = max(ans, min(abs(i-j), dp[i][j]))
    print(ans)
    # print(dp)
if __name__ == '__main__':
    main()
