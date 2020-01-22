import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from collections import defaultdict

def f(n):
    return (str(n)[0], str(n)[-1])

def main():
    n = int(input().strip())
    m = defaultdict(int)
    for i in range(1, n+1):
        m[f(i)] += 1
    ans = 0
    # print(m)
    for i in range(1, n+1):
        a, b = f(i)
        ans += m[(b, a)]
    print(ans)
if __name__ == '__main__':
    main()
