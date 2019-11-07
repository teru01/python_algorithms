import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
from collections import deque

def main():
    n, m = map(int, input().strip().split())
    nei = [[] for _ in range(n)]
    ans = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(lambda x: x-1, map(int, input().strip().split()))
        nei[a].append(b)
        nei[b].append(a)
    
    for i in range(n):
        c = 0
        for v in nei[i]:
            for w in nei[v]:
                if w != i and w not in nei[i] and w not in ans[i]:
                    ans[i].append(w)
                    c += 1
        print(c)

    # print(ans)
if __name__ == '__main__':
    main()
