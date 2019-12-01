import sys
input = sys.stdin.readline
from operator import itemgetter
INF = 10**30
sys.setrecursionlimit(10000000)
from collections import deque
G = []
into = [] # 入次数

def topological_sort(n):
    global into
    ans = []
    unvisited = [True] * n
    for i in range(n):
        if into[i] == 0 and unvisited[i]:
            q = deque()
            q.append(i)
            while len(q) > 0:
                node = q.popleft()
                ans.append(node)
                unvisited[node] = False
                for v in G[node]:
                    into[v] -= 1
                    if into[v] == 0:
                        q.append(v)
    return ans

# 再帰による実装
# visited = []
# answer = deque()
# def rec(v):
#     global visited
#     visited[v] = True

#     for node in G[v]:
#         if not visited[node]:
#             rec(node)
#     answer.appendleft(v)

# def dfs_topolo(n):
#     for i in range(n):
#         if not visited[i]:
#             rec(i)

def main():
    global G, into
    # global visited
    v, e = list(map(int, input().strip().split()))
    G = [[] for _ in range(v)]
    # visited = [False] * v
    into = [0] * v
    for i in range(e):
        s, t = list(map(int, input().strip().split()))
        G[s].append(t)
        into[t] += 1
    ans = topological_sort(v)
    for p in ans:
        print(p)
    # dfs_topolo(v)
    # for p in answer:
    #     print(p)

if __name__ == '__main__':
    main()
