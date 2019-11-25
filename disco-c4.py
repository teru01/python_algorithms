import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
M = []
w = 0
h = 0
num = 1
def solve2(p, q, r, s, ans):
    global num
    for i in range(p, q+1):
        for j in range(r, s+1):
            ans[i][j] = num
    num += 1
    return ans

def solve(p, q, ans):
    v = []
    for i in range(p, q+1):
        for j in range(w):
            if M[i][j] == '#':
                v.append(j)
    v.sort()
    prev = 0
    for i, b in enumerate(v):
        if i == len(v)-1:
            ans = solve2(p, q, prev, w-1, ans)
        else:
            ans = solve2(p, q, prev, b, ans)
            prev = b+1
    return ans

def main():
    global M, h, w
    h, w, k = list(map(int, input().strip().split()))
    M = [0] * h
    G = [False] * h
    ans = [[0] * w for _ in range(h)]
    total1Row = 0
    for i in range(h):
        M[i] = input().strip()
        if '#' in M[i]:
            G[i] = True
            total1Row += 1
    prev = 0
    vc = 0
    for i, v in enumerate(G):
        if v and vc == total1Row-1:
            ans = solve(prev, h-1, ans)
        elif v:
            vc += 1
            ans = solve(prev, i, ans)
            prev = i+1

    for i in range(h):
        print(" ".join(str(s) for s in ans[i]))

if __name__ == '__main__':
    main()
