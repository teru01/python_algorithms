import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def make_adj_list():
    n = int(input().strip()) # 頂点の数
    E = int(input().strip()) # 辺の数
    l = [[] for _ in range(n)] # 隣接リスト. 各要素は(コスト、to_node)
    for i in range(E):
        s, t, d = map(int, input().strip().split())
        l[s].append([d, t])
    return l

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    

if __name__ == '__main__':
    main()
