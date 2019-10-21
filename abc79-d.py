import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    h, w = map(int, input().strip().split())
    c = [[0] * 10 for _ in range(10)]
    for i in range(10):
        c[i] = list(map(int, input().strip().split()))
    a = [[0] * w for _ in range(h)]
    for i in range(h):
        a[i] = list(map(int, input().strip().split()))

    ary = list(c)
    for k in range(10):
        for i in range(10):
            for j in range(10):
                ary[i][j] = min(ary[i][j], ary[i][k] + ary[k][j])
    ans = 0
    for i in range(h):
        for j in range(w):
            if a[i][j] not in (-1, 1):
                # print(ary[i][j])
                ans += ary[a[i][j]][1]
    print(ans)
if __name__ == '__main__':
    main()
