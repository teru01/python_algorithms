import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    n, k = map(int, input().strip().split())
    a = sorted(list(map(int, input().strip().split())))
    f = sorted(list(map(int, input().strip().split())), reverse=True)

    l = -1
    r = 10**12
    while l+1 < r:
        mid = (l + r) // 2
        if sum(max(0, a[i] - mid/f[i]) for i in range(n)) <= k:
            r = mid
        else:
            l = mid
    print(r)

if __name__ == '__main__':
    main()
