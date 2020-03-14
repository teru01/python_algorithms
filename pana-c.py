import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from math import sqrt

def main():
    a, b, c = list(map(int, input().strip().split()))
    if c - a - b > 0 and 4 * a * b < (c - a - b) ** 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
