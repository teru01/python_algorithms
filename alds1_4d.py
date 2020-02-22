import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def n_load(p, k, n, w):
    i = 0
    load = 0
    tr = 0
    while i < n:
        if load + w[i] <= p:
            load += w[i]
            i += 1
        else:
            tr += 1
            if tr == k:
                break
            load = 0
    return i

def main():
    n, k = list(map(int, input().strip().split()))
    w = [0] * n
    for i in range(n):
        w[i] = int(input().strip())
    l = 0
    r = INF
    while l +1 < r:
        mid = (l + r) // 2
        ntr = n_load(mid, k, n, w)
        # print('ntr: ', ntr, l, r)
        if ntr == n:
            r = mid
        else:
            l = mid
    print(r)

if __name__ == '__main__':
    main()
