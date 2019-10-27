import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
from time import time

def is_prime(n):
    if n == 1:
        return 0
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return 0
        i += 1
    return 1

def main():
    q = int(input().strip())
    n = 10**5
    ary = [0] * (n+1)
    ary2 = [0] * (n+1)
    arys = [0] * (n+2)
    for i in range(2, n+1):
        ary[i] = is_prime(i)
    for i in range(1, n+1):
        ary2[i] = ary[i] & ary[(i+1)//2]
    for i in range(1, n+2):
        arys[i] = arys[i-1] + ary2[i-1]
    # print(ary[:20])
    # print(ary2[:20])
    # print(arys[:20])
    for i in range(q):
        l, r = map(int, input().strip().split())
        print(arys[r+1] - arys[l])

if __name__ == '__main__':
    main()
