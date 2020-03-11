import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n, m = list(map(int, input().strip().split()))
    a = []
    v = [1] * (n+1)
    w = [1] * (n+1)
    prev = -1
    for i in range(m):
        k = int(input().strip())
        a.append(k)
        v[k] = 0
    for c in reversed(a):
        if w[c] == 1:
            print(c)
            w[c] = 0
    for c in range(1, n+1):
        if v[c] == 1:
            print(c)

if __name__ == '__main__':
    main()
