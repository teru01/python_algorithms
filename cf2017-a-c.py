import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
from collections import defaultdict, Counter

def fail():
    print('No')
    sys.exit(0)

def suc():
    print('Yes')
    sys.exit(0)

def main():
    h, w = map(int, input().strip().split())
    mat = [0] * h
    d = {}
    for i in range(h):
        s = input().strip()
        for k, v in dict(Counter(s)).items():
            if k in d:
                d[k] += v
            else:
                d[k] = v
    if h % 2 == 1 and w % 2 == 1:
        g1 = 1
        g2 = h // 2 + w // 2
        g3 = (h // 2) * (w // 2)
    else:
        g1 = 0
        g2 = h // 2 + w // 2
        g3 = (h // 2) * (w // 2)

    for _ in range(g1):
        for k, v in d.items():
            if v % 4 == 1 or v % 4 == 3:
                d[k] -= 1
    for _ in range(g2):
        for k, v in d.items():
            if v % 4 == 2:
                d[k] = max(0, d[k] - 2)
    for _ in range(g3):
        for k, v in d.items():
            if v % 4 == 0:
                d[k] = max(0, d[k] - 4)
    if all(True if v == 0 else False for v in d.values()):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
