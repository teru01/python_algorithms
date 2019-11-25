import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    a = [0] * (n+1)
    for i in range(n):
        a[i+1] = a[i] + v[i]

if __name__ == '__main__':
    main()
