import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def dijkstra(n, start, nbl):
    """n: 頂点数, start: 始点, nbl: 隣接リスト"""
    import heapq
    WHITE = 1<<5
    GRAY = 1<<10
    BLACK = 1<<15
    INF = 1<<20
    color = [WHITE] * n
    distance = [INF] * n
    # parent = [-1] * n
    q = []

    distance[start] = 0
    heapq.heappush(q, (0, start))
    while len(q) != 0:
        du, u = heapq.heappop(q)
        # print("u: {}, du: {}".format(u, du))
        color[u] = BLACK
        if distance[u] < du:
            continue
        for next, cost in nbl[u]:
            if color[next] != BLACK and distance[u] + cost < distance[next]:
                distance[next] = distance[u] + cost
                color[next] = GRAY
                heapq.heappush(q, (distance[next], next))
    return distance


def main():
    n = int(input().strip())
    nb = [[] for _ in range(n)]
    for i in range(n):
        l = list(map(int, input().strip().split()))
        for j in range(l[1]):
            nb[i].append((l[2 + 2 * j], l[3 + 2 * j]))
    d = dijkstra(n, 0, nb)
    for i, v in enumerate(d):
        print(i, v)


if __name__ == '__main__':
    main()
