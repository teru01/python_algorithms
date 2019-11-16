import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def prim(G, root, n):
    import heapq
    BLACK = 1<<10
    WHITE = 1<<20
    nodes = [WHITE] * n
    d = [INF] * n
    d[root] = 0
    p = [0] * n
    p[root] = -1
    while True:
        mincost = INF

        # 探索
        for i in range(n):
            if d[i] < mincost and nodes[i] == WHITE:
                mincost = d[i]
                next = i
        if mincost == INF:
            break
        # 移動
        nodes[next] = BLACK

        # 伝播
        for i in range(n):
            if nodes[i] == WHITE and G[next][i] != INF:
                if G[next][i] < d[i]:
                    d[i] = G[next][i]
                    p[i] = next
    return d

def main():
    global M
    n = int(input().strip())
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        M[i] = list(map(lambda x: INF if x == -1 else x, map(int, input().strip().split())))
    d = prim(M, 0, n)
    print(sum(d))

if __name__ == '__main__':
    main()
