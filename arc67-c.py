import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30


def hurui(n):
    is_prime = [0] * (10**5)
    for i in range(2, n+1):
        is_prime[i] = 1
    for i in range(2, n+1):
        if is_prime[i] == 1:
            j = i*2
            while j <= n:
                is_prime[j] = 0
                j += i
    return is_prime

def main():
    n = int(input().strip())
    is_prime = hurui(n)
    ans = 1
    for i in range(2, n+1):
        if is_prime[i] == 1:
            c = 0
            for j in range(i, n+1):
                p = j
                while p % i == 0:
                    p //= i
                    c += 1
            ans *= (c+1)
            ans %= (10**9+7)
    print(ans)
if __name__ == '__main__':
    main()
