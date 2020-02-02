import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from collections import Counter

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    d = dict(Counter(v))
    ans = 0
    for val in d.values():
        if val > 1:
            ans += val - 1
    if ans % 2 == 0:
        print(n - ans)
    else:
        print(n - ans - 1)


if __name__ == '__main__':
    main()
