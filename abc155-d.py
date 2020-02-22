import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**20

# 一方をpに固定したとき、積がx未満になるペアの個数
def f(p, x, n, a):
    if p > 0:
        l = -1
        r = n
        while l + 1 < r:
            mid = (l + r) // 2
            if p * a[mid] < x:
                l = mid
            else:
                r = mid
        return l+1
    else:
        l = -1
        r = n
        while l + 1 < r:
            mid = (l + r)//2
            if p * a[mid] < x:
                r = mid
            else:
                l = mid
        return n-r

# x未満になる組み合わせ数がk未満ならTrue
def is_under(x, k, n, a):
    ans = 0
    for c in a:
        ans += f(c, x, n, a)
        if c**2 < x:
            ans -= 1
    ans /= 2
    return ans < k

def main():
    n, k = list(map(int, input().strip().split()))
    a = sorted(list(map(int, input().strip().split())))
    l = -INF
    r = INF
    while l + 1 < r:
        mid = (l+r)//2
        if is_under(mid, k, n, a):
            l = mid
        else:
            r = mid
    print(l)

if __name__ == '__main__':
    main()
