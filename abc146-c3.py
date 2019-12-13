import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    a, b, x = list(map(int, input().strip().split()))
    l = 0
    r = 10**9+1
    while l+1 < r:
        mid = (l + r)//2
        if a * mid + b * len(str(mid)) <= x:
            l = mid
        else:
            r = mid
    print(l)

if __name__ == '__main__':
    main()
