import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def rec(i, x, k, n, mat):
    if i == n:
        return x == 0
    for j in range(k):
        ans = rec(i+1, x^mat[i][j], k, n, mat)
        if ans:
            return True
    return False

def main():
    n, k = list(map(int, input().strip().split()))
    t = [0 for _ in range(n)]
    for i in range(n):
        t[i] = list(map(int, input().strip().split()))
    if rec(0, 0, k, n, t):
        print('Found')
    else:
        print('Nothing')

if __name__ == '__main__':
    main()
