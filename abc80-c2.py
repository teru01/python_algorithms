import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from itertools import permutations

def main():
    n = int(input().strip())
    f = [0] * n
    p = [[] for _ in range(n)]
    for i in range(n):
        tmp = list(map(int, input().strip().split()))
        for j in range(10):
            f[i] += tmp[9-j] << j
    for i in range(n):
        p[i] = list(map(int, input().strip().split()))
    ans = -INF
    for b in range(1, 2**10):
        m = 0
        for j in range(n):
            v = fun(f[j], b)
            m += p[j][v]
        ans = max(ans, m)
    print(ans)

def fun(f, q):
    return bin(f & q).count('1')

if __name__ == '__main__':
    main()
