import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n, k = list(map(int, input().strip().split()))
    q = 0
    q += (k-1) * (n-k) * 6
    q += (n-1) * 3
    q += 1
    p = n ** 3
    print(q / p)

if __name__ == '__main__':
    main()
