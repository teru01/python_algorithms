import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from collections import defaultdict

def main():
    n = int(input().strip())
    d = defaultdict(int)
    for i in range(1, n+1):
        ds = str(i)
        d[(ds[0], ds[-1])] += 1
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            si = str(i)
            sj = str(j)
            ans += d[(si, sj)] * d[(sj, si)]
    print(ans)


if __name__ == '__main__':
    main()
