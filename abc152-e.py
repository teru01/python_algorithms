import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
MOD = 10**9+7

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    a = v[0]
    lcm = v[0]
    for i in range(n):
        if i > 0:
            tmp = a
            a = gcd(a, v[i])
            c_lcm = tmp * v[i] // a
            lcm = c_lcm * lcm // gcd(c_lcm, lcm)
    ans = 0
    # for i in range(n):
    #     ans += lcm // v[i] % MOD
    # print(ans % MOD)
    for i in range(n):
        ans += lcm * pow(v[i], MOD-2, MOD)
    print(ans % MOD)


if __name__ == '__main__':
    main()
