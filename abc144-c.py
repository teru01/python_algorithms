import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
from math import sqrt

def get_yakusu(n):
    i = 1
    ans = []
    while i**2 <= n:
        if n % i == 0:
            ans.append((i, n//i))
        i += 1
    return ans

def main():
    n = int(input().strip())
    y = get_yakusu(n)
    ans = 10 ** 20
    for a, b in y:
        ans = min(ans, a-1+b-1)
    print(ans)
if __name__ == '__main__':
    main()
