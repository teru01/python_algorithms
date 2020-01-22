import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    h = int(input().strip())
    w = int(input().strip())
    n = int(input().strip())
    print((n + max(h, w) - 1) // max(h, w))

if __name__ == '__main__':
    main()
