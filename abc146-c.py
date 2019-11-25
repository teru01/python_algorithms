import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
a = b = x = 0

def dig(x):
    return len(str(x))


def rec(l, r):
    if l < r:
        mid = (l + r) // 2
        cost = a * mid + b * dig(mid)
        if cost < x:
            return rec(mid+1, r)
        elif cost > x:
            return rec(l, mid)
        elif x == cost:
            return mid
    else:
        return max(l-1, 0)

def main():
    global a, b, x
    a, b, x = list(map(int, input().strip().split()))
    q = rec(0, x)
    if q > 10**9:
        print(10**9)
    else:
        print(rec(0, x))

if __name__ == '__main__':
    main()
