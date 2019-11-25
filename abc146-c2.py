import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    a, b, x = list(map(int, input().strip().split()))
    ans = 0
    for d in range(1, 20):
        n = (x - b*d) // a
        if n < 0:
            continue
        if len(str(n)) == d:
            ans = max(ans, n)
            print("d:", d)
    print(min(ans, 10**9))

if __name__ == '__main__':
    main()

#10**9 * n + 10**9 * d < 10**18
