import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from itertools import combinations_with_replacement

def main():
    n = int(input().strip())
    v = input().strip()
    dp = [0] * (n+1)
    ans = INF
    for i in range(n):
        dp[i+1] = i+1
    lis = ['A', 'B', 'X', 'Y']
    for c in lis:
        for d in lis:
            for e in lis:
                for f in lis:
                    for i in range(n):
                        dp[i+1] = i+1
                    flag = False
                    for i in range(1, n):
                        if not flag and ((v[i-1] == c and v[i] == d) or (v[i-1] == e and v[i] == f)):
                            dp[i+1] = dp[i]
                            flag = True
                        else:
                            dp[i+1] = dp[i] + 1
                            flag = False
                    # print(c, d, e, f, end='')
                    # print(dp)
                    ans = min(ans, dp[n])
    print(ans)

if __name__ == '__main__':
    main()
