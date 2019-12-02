import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from collections import Counter
from math import factorial

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    l = [0] * n
    for i in range(n):
        l[i] = abs(n-2*i-1)
    if sorted(v) != sorted(l):
        print(0)
        return
    c = dict(Counter(l))
    ans = 1
    d = 10**9 + 7
    for v in c.values():
        ans *= factorial(v) % d
    print(ans % d)

if __name__ == '__main__':
    main()
