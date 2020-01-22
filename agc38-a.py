import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    h, w, wa, hb = list(map(int, input().strip().split()))
    for i in range(h):
        if i < hb:
            print('0' * wa + '1' * (w-wa))
        else:
            print('1' * wa + '0' * (w-wa))


if __name__ == '__main__':
    main()
