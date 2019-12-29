import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    v.sort()
    M = v[-1]
    d = INF
    ans = -1
    for c in v[:-1]:
        if abs(c - M//2) <= d:
            d = abs(c - M//2)
            ans = c
    print(M, ans)


if __name__ == '__main__':
    main()
