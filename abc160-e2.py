import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    x, y, a, b, c = list(map(int, input().strip().split()))
    p = sorted(list(map(int, input().strip().split())), reverse=True)
    q = sorted(list(map(int, input().strip().split())), reverse=True)
    r = sorted(list(map(int, input().strip().split())), reverse=True)
    print(sum(sorted((p[:x]+q[:y]+r), reverse=True)[:x+y]))

if __name__ == '__main__':
    main()
