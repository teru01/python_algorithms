import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n, k = map(int, input().strip().split())
    r = list(map(int, input().strip().split()))
    v = sorted(r, reverse=True)[:k]
    ans = 0
    for i in range(k):
        ans += 2**(k-1-i) * v[i]
    print(ans / 2**k)
if __name__ == '__main__': 
    main()
