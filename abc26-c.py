import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

class Node:
    def __init__(self):
        self.children = []

nodes = []

def rec(i):
    if len(nodes[i].children) == 0:
        return 1
    return max(rec(c) for c in nodes[i].children) + min(rec(c) for c in nodes[i].children) + 1

def deb_p(nodes):
    for i, n in enumerate(nodes):
        print("{}: children: {}".format(i, n.children))

def main():
    global nodes
    n = int(input().strip())
    p = [0] * n
    nodes = [Node() for _ in range(n)]
    for i in range(1, n):
        p[i] = int(input().strip()) - 1
        nodes[p[i]].children.append(i)
    # deb_p(nodes)
    print(rec(0))

if __name__ == '__main__':
    main()
