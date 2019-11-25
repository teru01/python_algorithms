import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    while True:
        n, k = list(map(int, input().strip().split()))
        if n == 0 and k == 0:
            return
        v = [0] * n
        a = [0] * (n+1)
        for i in range(n):
            v[i] = int(input().strip())
        for i in range(n):
            a[i+1] = v[i] + a[i]

        ans = -INF
        for i in range(n-k+1):
            ans = max(ans, a[i+k] - a[i])
        print(ans)

if __name__ == '__main__':
    main()
