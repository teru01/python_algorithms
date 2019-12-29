import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    h, w = list(map(int, input().strip().split()))
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    c = [[0] * w for _ in range(h)]
    k = 1
    l = 0
    for i in range(h):
        for j in range(w):
            if i % 2 == 0:
                c[i][j] = k
            else:
                c[i][w-1-j] = k
            a[l] -= 1
            if a[l] == 0:
                k += 1
                l += 1
    for i in range(h):
        print(' '.join(map(str, c[i])))

if __name__ == '__main__':
    main()
