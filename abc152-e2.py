import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    g = v[0]
    for i in v:
        t = g
        g = gcd(g, i)

if __name__ == '__main__':
    main()
