import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    k, t = list(map(int, input().strip().split()))
    v = list(map(int, input().strip().split()))
    v.sort(reverse=True)
    if len(v) > 1:
        print(v[0]-1 - min(v[0]-1, sum(v[1:])))
    else:
        print(v[0]-1)

if __name__ == '__main__':
    main()
