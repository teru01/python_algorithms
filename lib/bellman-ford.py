import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def make_adj_list(n, E):
    l = [[] for _ in range(n)] # 隣接リスト. 各要素は(コスト、to_node)
    for i in range(E):
        s, t, d = map(int, input().strip().split())
        l[s].append([d, t])
    return l

# 全てのエッジに関してtoの最短距離を更新、それを頂点回数繰り返す
# エッジ1周につき最低1頂点は最短距離が求まるのでそれを伝播させていく
def bellman_ford(n, s, l):
    # s: start node, n: num of node
    # return True: negative cycle
    dist = [INF] * n
    dist[s] = 0
    for i in range(n):
        # 全てのエッジに関してtoの最短距離を更新
        for v in range(n):
            for k in range(len(l[v])):
                cost, to = l[v][k]
                if dist[v] != INF and dist[to] > dist[v] + cost:
                    dist[to] = dist[v] + cost
                    if i == n-1:
                        return (True, dist)
    return (False, dist)

def main():
    v, e, r = map(int, input().strip().split())
    l = make_adj_list(v, e)
    is_negative_cycle, dist = bellman_ford(v, r, l)
    if is_negative_cycle:
        print("NEGATIVE CYCLE")
        return
    for d in dist:
        if d == INF:
            print('INF')
        else:
            print(d)

if __name__ == '__main__':
    main()
