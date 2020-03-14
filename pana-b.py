import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    h, w = list(map(int, input().strip().split()))
    if h == 1 or w == 1:
        print(1)
    else:
        print((h * w + 1) // 2)

if __name__ == '__main__':
    main()
