import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
import itertools
from math import sqrt, factorial

def main():
    n = int(input().strip())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().strip().split())
    s = [0] * factorial(n)
    for k, perm in enumerate(itertools.permutations(range(n), n)):
        s[k] = 0
        for ind, i in enumerate(perm):
            if ind == 0:
                px, py = x[i], y[i]
                continue
            s[k] += sqrt((x[i] - px)**2 + (y[i] - py) ** 2)
            px, py = x[i], y[i]
    print(sum(s) / len(s))
    


if __name__ == '__main__':
    main()
