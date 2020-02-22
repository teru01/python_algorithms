import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from collections import Counter

def main():
    v = list(map(int, input().strip().split()))
    if len(Counter(v)) == 2:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main()
