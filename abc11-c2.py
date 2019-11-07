import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    ngs = [a, b, c]
    dp = [10**9] * 305
    dp[n] = 0
    for i in reversed(range(n+1)):
        if i in ngs:
            continue
        for j in [1, 2, 3]:
            dp[i-j] = min(dp[i] + 1, dp[i-j])
    if dp[0] > 100:
        print('NO')
    else:
        print('YES')
    # print(dp)

if __name__ == '__main__':
    main()
