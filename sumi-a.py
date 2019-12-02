import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    m1, d1 = list(map(int, input().strip().split()))
    m2, d2 = list(map(int, input().strip().split()))
    if m1 != m2:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
