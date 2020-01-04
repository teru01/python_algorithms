import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def gcd(a, b):
    if a % b != 0:
        return gcd(b, a % b)
    else:
        return b

def main():
    a, b = list(map(int, input().strip().split()))
    g = gcd(a, b)
    # is_prime = hurui(10**6+10)
    i = 2
    c = 0
    # print(g)
    ans = []
    while i**2 <= g:
        if g % i == 0:
            ans.append([i, 0])
            while g % i == 0:
                g /= i
                ans[-1][1] += 1
        i += 1
    if g != 1:
        ans.append([g, 1])
    # print(ans)
    print(len(ans)+1)

if __name__ == '__main__':
    main()
