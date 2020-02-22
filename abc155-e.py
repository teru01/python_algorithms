import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    v = input().strip()
    w = list(reversed(v))
    ans = 0
    for i, c in enumerate(w):
        d = int(c)
        if d <= 5:
            k = d
        else:
            k = 11 - d
        print(ans)
        if i == 0:
            ans = k
        else:
            ans = min(ans + k, ans + k - 1 - int(w[i-1]))
    print(ans)

if __name__ == '__main__':
    main()
