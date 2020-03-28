import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n, m = list(map(int, input().strip().split()))
    print(n * max(0, n-1) // 2 + m * max(0, m-1) // 2)

if __name__ == '__main__':
    main()
