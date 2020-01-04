import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def keta(n):
    return len(str(n))

def main():
    n = int(input().strip())
    i = 1
    ans = INF
    while i**2 <= n:
        if n % i == 0:
            ans = min(ans, max(keta(i), keta(n//i)))
        i += 1
    print(ans)

if __name__ == '__main__':
    main()
