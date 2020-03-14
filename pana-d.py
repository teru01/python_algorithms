import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

A = "abcdefghij"
N = 0
def dfs(s, n, prev):
    global N
    if len(s) == N:
        print("".join(s))
        # s = []
        return
    s.append(A[prev])
    print(s)
    dfs(s, n+1, prev)
    s[-1] = A[prev + 1]
    dfs(s, n+1, prev+1)

def main():
    global N
    N = int(input().strip())
    dfs([], 0, 0)

if __name__ == '__main__':
    main()
