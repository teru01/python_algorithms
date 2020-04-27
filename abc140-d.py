import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n, k = list(map(int, input().strip().split()))
    s = input().strip()
    q = 0
    p = ''
    for c in s:
        if c != p:
            q += 1
        p = c
    # print(q)
    print(min(n-1, n - q + 2 * k))

if __name__ == '__main__':
    main()
