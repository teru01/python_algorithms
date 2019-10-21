import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
from collections import deque

# 頂点を1度づつ訪れて隣接リストをたどるのでO(|V| + |E|)
def main():
    n, m = map(int, input().strip().split())
    nei = [[] for _ in range(n)]
    for _ in range(m):
        s, t = map(int, input().strip().split())
        nei[s].append(t)
        nei[t].append(s)

    nodes = [-1] * n
    color = 1
    for i in range(n):
        if nodes[i] > 0:
            continue
        d = deque()
        d.append(i)
        # print(nei)
        while len(d) != 0:
            k = d.popleft()
            nodes[k] = color
            for j in nei[k]:
                if nodes[j] == -1:
                    d.append(j)
            # print(len(d))
        color += 1

    q = int(input().strip())
    for _ in range(q):
        s, t = map(int, input().strip().split())
        if nodes[s] == nodes[t]:
            print('yes')
        else:
            print('no')

if __name__ == '__main__':
    main()
