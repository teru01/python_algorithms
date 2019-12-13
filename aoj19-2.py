import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
G = []
from collections import deque, defaultdict

def zeropos(v):
    v.index(0)

def main():
    v = [0] * 9
    for i in range(3):
        v[3 * i: 3*i+3] = list(map(int, input().strip().split()))
    already = defaultdict(bool)
    q = deque()
    last = list(range(1, 9)) + [0]
    q.append((v, 0))
    while len(q) > 0:
        l, swapcount = q.popleft()
        if l == last:
            print(swapcount)
            # print(len(already))
            return
        zp = l.index(0)
        if zp not in [0, 1, 2]:
            next = list(l)
            next[zp-3], next[zp] = next[zp], next[zp-3]
            if not already[tuple(next)]:
                already[tuple(next)] = True
                q.append((next, swapcount+1))
        if zp not in [0, 3, 6]:
            next = list(l)
            next[zp-1], next[zp] = next[zp], next[zp-1]
            if not already[tuple(next)]:
                already[tuple(next)]
                q.append((next, swapcount+1))

        if zp not in [6, 7, 8]:
            next = list(l)
            next[zp+3], next[zp] = next[zp], next[zp+3]
            if not already[tuple(next)]:
                already[tuple(next)]
                q.append((next, swapcount+1))

        if zp not in [2, 5, 8]:
            next = list(l)
            next[zp+1], next[zp] = next[zp], next[zp+1]
            if not already[tuple(next)]:
                already[tuple(next)]
                q.append((next, swapcount+1))

if __name__ == '__main__':
    main()
