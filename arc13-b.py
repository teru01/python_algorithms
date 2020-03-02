import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    N = []
    M = []
    L = []
    for i in range(n):
        a = list(map(int, input().strip().split()))
        a.sort()
        N.append(a[0])
        M.append(a[1])
        L.append(a[2])
    print(max(N) * max(M) * max(L))

if __name__ == '__main__':
    main()
