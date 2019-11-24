import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def make_comb(m, d):
    def div(i, j):
        # 1/i mod(j)
        # calc i**(j-2) mod(j)
        p = j - 2
        ans = 1
        while p != 0:
            if p % 2 == 1:
                ans = (ans * i) % d
            i = i**2 % d
            p >>= 1
        return ans

    fac = [0] * (m+1)
    ifac = [0] * (m+1)
    # nCk
    fac[0] = 1
    ifac[0] = 1
    for i in range(m):
        fac[i+1] = (fac[i] * (i+1)) % d
        ifac[i+1] = (ifac[i] * div(i+1, d)) % d
    def comb(n, k):
        if n == 0 and k == 0:
            return 1
        if n < k or n < 0:
            return 0
        return (fac[n] * ifac[k] * ifac[n-k]) % d
    return comb

def main():
    comb = make_comb(10**6, 10**9 + 7)
    # calc 10C2
    print(comb(10, 2))
    print(comb(5, 2))

if __name__ == '__main__':
    main()
