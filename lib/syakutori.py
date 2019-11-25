import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n, q = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    x = list(map(int, input().strip().split()))
    for v in x:
        j = 0
        s = 0
        ans = 0
        for i in range(n):
            while j < n and s + a[j] <= v:
                s += a[j]
                j += 1
            ans += j - i
            if j == i:
                j += 1
            else:
                s -= a[i]
        print(ans)

if __name__ == '__main__':
    main()
