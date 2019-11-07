import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

M = [[[[-1] * 100 for _ in range(100)] for _ in range(100)] for _ in range(300)]
ngs = []

def rec(n, s, t, u):
    if n < 0 or n in ngs or s < 0 or t < 0 or u < 0:
        M[n][s][t][u] = False
        return False
    if n == 0:
        M[n][s][t][u] = True
        return True
    if M[n][s][t][u] != -1:
        return M[n][s][t][u]

    M[n][s][t][u] = rec(n-1, s-1, t, u) or rec(n-2, s, t-1, u) or rec(n-3, s, t, u-1)
    return M[n][s][t][u]


def main():
    global ngs
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    ngs.extend([a, b, c])
    for s in range(101):
        for t in range(101 - s):
            if n % 3 * (100 - s - t) == 0:
                u = 100 - s - t
                if rec(n, s, t, u):
                    return 'Yes'


if __name__ == '__main__':
    main()
