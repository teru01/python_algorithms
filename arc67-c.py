import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def calc_prime(n):
    ans = []
    for i in range(2, n):
        if is_prime(i):
            ans.append(i)
    return ans

primes = []
def calc_divisor(n):
    

def main():
    global primes
    n = int(input().strip())
    primes = calc_prime(n)
    ans = 0
    d = 10**9+7
    

    for i in range(1, n):
        ans += comb(n-1, i)
        print(ans)
    print((ans+1) % d)

if __name__ == '__main__':
    main()
