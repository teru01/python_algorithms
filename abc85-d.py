import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n, h = map(int, input().strip().split())
    p = []
    for i in range(n):
        a, b = map(int, input().strip().split())
        p.append((a, 0))
        p.append((b, 1))
    p.sort(reverse=True)
    s = 0
    i = 0
    ans = 0
    while s < h:
        s += p[i][0]
        ans += 1
        if p[i][1] == 1:
            i += 1
        else:
            ans += (h - s + p[i][0]-1) // p[i][0]
            break
    print(ans)
if __name__ == '__main__':
    main()
