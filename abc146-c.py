import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
a = b = x = 0

def dig(x):
    return len(str(x))

def rec(l, r):
    if l+1 < r:
        mid = (l + r) // 2
        cost = a * mid + b * dig(mid)
        if cost < x:
            return rec(mid, r)
        elif cost > x:
            return rec(l, mid)
        elif x == cost:
            return mid
    else:
        return l

def main():
    global a, b, x
    a, b, x = list(map(int, input().strip().split()))
    l = 0
    r = 10**9
    while l+1 < r:
        mid = (l+r)//2
        cost = a * mid + b * dig(mid)
        if cost <= x:
            l = mid
        else:
            r = mid
    
    # q = rec(0, x)
    q = l
    if q > 10**9:
        print(10**9)
    else:
        print(rec(0, x))

if __name__ == '__main__':
    main()
