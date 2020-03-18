import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from itertools import combinations

def main():
    n = int(input().strip())
    G = [[-1] * n for _ in range(n)]
    # H = [[0] * n for _ in range(n)]
    for i in range(n):
        m = int(input().strip())
        for j in range(m):
            x, y = list(map(int, input().strip().split()))
            G[i][x-1] = y
    # print(G)
    for i in reversed(range(n+1)):# n~0
        for c in combinations(range(n), i):
            # 正直者と正直者が指す人，がある特定の人を正直，真偽不明で指していたら矛盾
            cont = False
            # print("c: ", c)
            for p in c:
                for j in range(n):
                    if G[p][j] == -1:
                        continue
                    if (G[p][j] == 1) != (j in c):
                        cont = True
                    # print("p, j, cont: ", p, j, cont)
                    # print(c, j in c)
                    # print(G[p][j] == 1)
                    # print((G[p][j] == 1) != True)
                    # if (j in c and G[p][j] == 0):
                    #     print("cont: ", c)
                    #     cont = True
            if cont == False:
                print(i)
                return

if __name__ == '__main__':
    main()
