import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from copy import deepcopy
from collections import Counter


def dfs(G, i, fr, color):
    color[i] = 1
    for node in G[i]:
        if node != fr and node != -1 and color[node] == -1:
            dfs(G, node, i, color)

def main():
    n, m = list(map(int, input().strip().split()))
    G = [[] for _ in range(n)]
    for i in range(m):
        a, b = list(map(int, input().strip().split()))
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    ans = 0
    for i, node in enumerate(G):
        for j, edge in enumerate(G[i]):
            D = deepcopy(G)
            D[i][j] = -1
            color = [-1] * n
            dfs(D, 0, -1, color)
            c = Counter(color)[1]
            if c != n:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
