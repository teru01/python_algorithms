import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from collections import Counter
G = []
H = []
color = []


def dfs(G, i, fr, c):
    global color
    color[i] = c
    # print('lp')
    for node in G[i]:
        if color[node] == -1:
            dfs(G, node, i, c)


def main():
    global G, H, color
    n, m, k = list(map(int, input().strip().split()))
    G = [[] for _ in range(n)]
    H = [[] for _ in range(n)]
    color = [-1] * n
    for i in range(m):
        a, b = list(map(lambda x: x-1, map(int, input().strip().split())))
        G[a].append(b)
        G[b].append(a)
    for i in range(k):
        a, b = list(map(lambda x: x-1, map(int, input().strip().split())))
        H[a].append(b)
        H[b].append(a)
    c = 0
    # print(G)
    for i in range(n):
        # print('before dfs')
        if color[i] == -1:
            dfs(G, i, -1, c)
            c += 1
        # print('af dfs')
    counter = dict(Counter(color))
    # print(counter)
    # print(color)
    # print(H)
    for i in range(n):
        block = 0
        for b in H[i]:
            if color[i] == color[b]:
                block += 1
        # print('block, ', block)
        print(counter[color[i]] - 1 - len(G[i]) - block)

if __name__ == '__main__':
    main()
