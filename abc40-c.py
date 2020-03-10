import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    now = v[0]
    ans = [0] * n
    ans[1] = abs(v[1] - v[0])
    i = 2
    while i < n:
        ans[i] = min(ans[i-1] + abs(v[i] - v[i-1]), ans[i-2] + abs(v[i] - v[i-2]))
        i += 1
    print(ans[n-1])

if __name__ == '__main__':
    main()
