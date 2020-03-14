import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from bisect import bisect_left

def main():
    n, m = list(map(int, input().strip().split()))
    x, y = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    a_i = 0
    ans = 0
    while a_i < n:
        b_i = bisect_left(b, a[a_i] + x)
        if b_i >= m:
            break
        a_i = bisect_left(a, b[b_i] + y)
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
