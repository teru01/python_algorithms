import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

np = 0

def make_tree(l, r, P, T):
    """T = [(location, left, right), (), ...]"""
    global np
    if l >= r:
        return None
    P[l:r].sort()
    mid = (l + r) // 2
    np += 1
    t = np
    T[t][0] = mid # Pにおける位置

    # print("np: ", np)
    
    lind = make_tree(l, mid, P, T) # 左ノードのインデックス
    T[t][1] = lind
    # print("lind: ", lind)
    
    rind = make_tree(mid+1, r, P, T)
    T[t][2] = rind
    print("rind: ", rind)
    return np

c = 0
def find(v, sx, tx, P, T):
    x = P[T[v][0]]
    # print(v)
    if sx <= x and x <= tx:
        print(P[T[v][0]])
    if T[v][1] != None and sx <= x:
        find(T[v][1], sx, tx, P, T)
    if T[v][2] != None and x <= tx:
        find(T[v][2], sx, tx, P, T)

def main():
    n = int(input().strip())
    P = list(map(int, input().strip().split()))
    T = [[0, 0, 0] for _ in range(n+1)]
    make_tree(0, n, P, T)
    for i in range(len(T)):
        print(T[i])
    find(1, 6, 15, P, T)

if __name__ == '__main__':
    main()
