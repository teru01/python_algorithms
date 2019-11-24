import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))

    a = [0] * n
    b = [0] * n
    for i in range(n):
        if i == 0:
            a[i] = v[i]
            continue
        a[i] = a[i-1] + v[i]
    for i in reversed(range(n)):
        if i == n-1:
            b[i] = v[i]
            continue
        b[i] = b[i+1] + v[i]
    ans = INF
    for i in range(n-1):
        ans = min(ans, abs(a[i] - b[i+1]))
    print(ans)
if __name__ == '__main__':
    main()
