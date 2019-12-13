import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from itertools import accumulate

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    v.sort()
    s = [0] + list(accumulate(v))
    ans = 0
    for i in range(1, n):
        if 2 * s[i] >= v[i]:
            ans += 1
        else:
            ans = 0
    ans += 1
    print(ans)

if __name__ == '__main__':
    main()
