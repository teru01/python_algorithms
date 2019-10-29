import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

a = []
f = []
n = 0

def rec(l, r, k):
    if l+1 < r:
        mid = (l + r) // 2
        s = 0
        for i in range(n):
            s += max(a[i] - mid // f[i], 0)
        if s <= k:
            return rec(l, mid, k)
        else:
            return rec(mid, r, k)
    else:
        return r

def main():
    global a, f, n
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    f = list(map(int, input().strip().split()))
    a = sorted(a)
    f = sorted(f, reverse=True)
    print(rec(-1, 10**12, k))

if __name__ == '__main__':
    main()
