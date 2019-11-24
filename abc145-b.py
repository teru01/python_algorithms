import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    v = input().strip()
    if n % 2 == 1:
        print('No')
        return
    if v[:n//2] == v[n//2:]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
