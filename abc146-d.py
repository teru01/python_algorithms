import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from collections import deque

def main():
    n = int(input().strip())
    G = [[] for _ in range(n)]
    A = [0] * n
    B = [0] * n
    for i in range(n-1):
        a, b = list(map(int, input().strip().split()))
        A[i] = a
        B[i] = b
        G[a-1].append([b-1, 0])
        G[b-1].append([a-1, 0])
    root = 0
    mlen = len(G[0])
    for i in range(n):
        if mlen < len(G[i]):
            mlen = len(G[i])
            root = i
    nodes = [0] * n
    q = deque()
    q.append((root, -1))
    while len(q) > 0:
        v, fr = q.popleft()
        for y, (w, _) in enumerate(G[v]):
            color = 1
            if w != fr:
                if fr == -1:
                    print(v, w)
                    G[v][y][1] = color
                elif G[v][fr][1] != color:
                    G[v][y][1] = color
                else:
                    color += 1
                    G[v][w][1] = color
                q.append((w, v))
                color += 1
    for i in range(n):
        print(G[i])
if __name__ == '__main__':
    main()
