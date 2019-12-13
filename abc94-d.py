import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    v.sort()
    fac = [1]
    for i in range(1, n+1):
        fac.append(fac[-1] * i)
    m = INF
    ans = -1
    for r in range(0, n+1):
        c = fac[r] * fac[n-r]
        if c < m:
            m = c
            ans = r
    print()


if __name__ == '__main__':
    main()
