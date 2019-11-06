import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
from collections import Counter

def main():
    n = int(input().strip())
    p = []
    for i in range(n):
        x, y = map(int, input().strip().split())
        p.append((x, y))
    vtable = [0] * n**2
    for i in range(n):
        for j in range(n):
            vtable[i * n + j] = (p[i][0] - p[j][0], p[i][1] - p[j][1])
    c = sorted(Counter(vtable).values(), reverse=True)
    if len(c) == 1:
        print(1)
    else:
        print(n - c[1])


if __name__ == '__main__':
    main()
