import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from itertools import permutations

def main():
    n, m, l = list(map(int, input().strip().split()))
    p, q, r = list(map(int, input().strip().split()))
    ans = 0
    for x, y, z in permutations([p, q, r]):
        ans = max(ans, (n // x) * (m // y) * (l // z))
    print(ans)
if __name__ == '__main__':
    main()
