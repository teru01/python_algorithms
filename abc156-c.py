import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    ans = INF
    for i in range(1, 101):
        t = 0
        for j in range(n):
            t += (i - v[j]) ** 2
        ans = min(ans, t)
    print(ans)

if __name__ == '__main__':
    main()
