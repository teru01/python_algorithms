import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
from math import sqrt

def get_yakusu(n):
    i = int(sqrt(n))
    while i > 0:
        if n // i > 10 ** 9:
            return -1, -1
        if n % i == 0:
            return i, n//i
        i -= 1

def rec(left, right, n, S, a):
    if left == right:
        return left
    mid = (left + right) // 2
    if mid <= n:
        return rec(mid, right, n)
    else:
        return rec(left, mid, n)

def main():
    S = int(input().strip())
    y2 = (S+10**9-1) // 10**9
    y1 = 10**9 * y2 - S
    print("0 0 {} {} {} {}".format(10**9, y1, 1, y2))

if __name__ == '__main__':
    main()
