import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    # w = [0] * n
    h = []
    for i in range(n):
        w = int(input().strip())
        m = INF
        for j, v in enumerate(h):
            if v >= w:
                if m > v:
                    m = v
                    t = j
        if m == INF:
            h.append(w)
        else:
            h[t] = w
    print(len(h))

if __name__ == '__main__':
    main()
