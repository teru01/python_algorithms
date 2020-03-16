import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

A = "abcdefghij"
N = 0
def dfs(s, lim):
    global N
    if len(s) == N:
        print("".join(s))
        # s = []
        return
    for i in range(lim): # abacなどが入らない
        s.append(A[i])
        dfs(s, len(set(s)) + 1)
        s.pop()
    # print(s)
    # dfs(s, prev)
    # s[-1] = A[prev + 1]
    # dfs(s, n+1, prev+1)

def main():
    global N
    N = int(input().strip())
    dfs([], 1)

if __name__ == '__main__':
    main()
