import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
    n = int(input().strip())
    s = input().strip()
    dp = [[0] * (n+1) for _ in range(n+1)]
    # dp[n-1][n-1] = 1
    ans = 0
    for i in reversed(range(n)):
        for j in reversed(range(n)):
            if s[i] == s[j]:
                dp[i][j] = min(abs(j - i), dp[i+1][j+1] + 1)
            ans = max(ans, dp[i][j])
    print(ans)
if __name__ == '__main__':
    main()
