import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    x, y, a, b, c = list(map(int, input().strip().split()))
    p = sorted(list(map(int, input().strip().split())), reverse=True)[:x]
    q = sorted(list(map(int, input().strip().split())), reverse=True)[:y]
    r = sorted(list(map(int, input().strip().split())), reverse=True)
    print(sum(sorted(p + q + r, reverse=True)[:x+y]))
if __name__ == '__main__':
    main()
