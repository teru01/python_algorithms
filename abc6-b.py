import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
MOD = 10007
def main():
    n = int(input().strip())
    if n == 1 or n == 2:
        print(0)
        return
    elif n == 3:
        print(1)
        return
    p = 1
    pp = 0
    ppp = 0
    for i in range(4, n+1):
        ans = p + pp + ppp
        ppp = pp
        pp = p
        p = ans % MOD
        # print(ans)
    print(ans % MOD)

if __name__ == '__main__':
    main()
