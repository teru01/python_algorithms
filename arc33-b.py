import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    na, nb = list(map(int, input().strip().split()))
    a = set(map(int, input().strip().split()))
    b = set(map(int, input().strip().split()))
    print(len(a.intersection(b)) / len(a.union(b)))

if __name__ == '__main__':
    main()
