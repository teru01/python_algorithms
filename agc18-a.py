import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

def main():
    n, q = list(map(int, input().strip().split()))
    v = list(map(int, input().strip().split()))
    v.sort()
    k = v[0]
    for i in range(1, n):
        k = gcd(v[i], k)
    if q <= v[-1] and q % k == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()
