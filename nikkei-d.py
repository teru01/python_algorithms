#          .g          `
#       .J.,M|  ..+NMMJMMMMNg..     `        `      `   `
#       ?TMa,5.MMMMMMM?MMMMMMMMt    _Z771,   (w.  j771. j_  z  `  `  `  `  `
#      dNHk;.NMMMB3???<ZZZZZW#^  `  _I  (Z  -C?l  j_  O j_  z`                `
#         .dMMM3_1????{ZZZZX=       _Ozr>`  J>.z_ jIz7! j7?7O`
#    `    dMMM!..__1=?>wZZC`        _I _O. (>  ?I j_    j_  z`
#        .MMM%.._Tm,?1>z0^          _C  _1.J`   (:j`    j`  z`   `  `  `  `  `
#        .Hmm..-?=!..``-gNNg-...`                -.
#     `  JMMMz>>????<<..WMMMMMMMMNe              !_                            `
#        ,MMMp?>?<<(;:(yI1rrwVMMMMM| z771.  `(v-  (C71+ (}  (:  `
#         WMMN<<(::;:!dyyIjtrrrdMMM\`O   w~  J<I  (}  (:(}  ({     `  `  `  `
#    `  `  TgMNx;;:;;(yyyyn1trqMMM# .OvO2!  (l.({ (Izv^ (C771{         .. .. .,
#           TMMMNgJ+!dyyyyynjMMMM#! `O _1. .v~`~z.(}    (}  ({    O?z(_.J..o.l,
#            .TMMMMM(MMMMMMMNWMM"    O  `1-(:   (l(}    (}  ({
#     `          ?""WMMMMMMW9^
#       `                                                      `


import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def dijkstra(n, start, nbl):
    """n: 頂点数, start: 始点, nbl: 隣接リスト"""
    import heapq
    WHITE = 1<<5
    GRAY = 1<<10
    BLACK = 1<<15
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
    n, m = map(int, input().strip().split())
    nbl = [[] for _ in range(n)]
    for i in range(n-1):
        nbl[i+1].append((i, 0))
    for i in range(m):
        l, r, c = map(int, input().strip().split())
        l -= 1
        r -= 1
        nbl[l].append((r, c))
    d = dijkstra(n, 0, nbl)
    if d[-1] == INF:
        print(-1)
    else:
        print(d[-1])

if __name__ == '__main__':
    main()
