import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
MOD = 10**9 + 7

def main():
    n, m = list(map(int, input().strip().split()))
    if (n % MOD) // (m % MOD) == (n * pow(m, MOD-2, MOD)) % MOD:
        print('Equal')
    print((n // m) % MOD)
    print((n * pow(m, MOD-2, MOD)) % MOD)

if __name__ == '__main__':
    main()
