import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    i = 2
    ans = []
    while i**2 <= n:
        if n % i == 0:
            ans.append([i, 0])
            while n % i == 0:
                n //= i
                ans[-1][1] += 1
        i += 1
    if n != 1:
        ans.append([n, 1])
    print(ans)

if __name__ == '__main__':
    main()
