import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

tmp = []
tree = []

def dfs(node, depth, fr):
    global tmp, tree
    tree[node] = (fr, depth)
    for i, c in tmp[node]:
        if i != fr:
            dfs(i, depth+c, node)

def main():
    global tmp, tree
    n = int(input().strip())
    tmp = [[] for _ in range(n)]
    tree = [0] * n
    for _ in range(n-1):
        a, b, c = map(int, input().strip().split())
        a -= 1
        b -= 1

        if b > a:
            a, b = b, a
        tmp[a].append((b, c))
        tmp[b].append((a, c))

    q, k = map(int, input().strip().split())
    k -= 1
    dfs(k, 0, -1)
    # print(tmp)
    # print(tree)
    for _ in range(q):
        x, y = map(lambda x: x-1, map(int, input().strip().split()))
        print(tree[x][1] + tree[y][1])


if __name__ == '__main__':
    main()
