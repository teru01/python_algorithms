import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    h, w, k = list(map(int, input().strip().split()))
    M = [[0] * w for _ in range(h)]
    ans = [[0] * w for _ in range(h)]
    row = [-1] * h
    G = [False] * h
    for i in range(h):
        M[i] = input().strip()
        G[i] = any(True if v == '#' else False for v in M[i])
    prev = 0
    id = 1
    for i, v in enumerate(G):
        if v:
            for j, b in enumerate(M[i]):
                if b == '#':
                    ans[i][j] = id
                    id += 1
                    continue
                if j == 0:
                    ans[i][j] = id
                else:
                    ans[i][j] = ans[i][j-1]
            for p in range(prev, i):
                ans[p] = list(ans[i])
            prev = i+1
        else:
            if i == h-1:
                ans[i] = list(ans[i-1])
    for i in range(h):
        print(" ".join(str(c) for c in ans[i]))


if __name__ == '__main__':
    main()
