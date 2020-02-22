import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    for c in v:
        if c % 2 == 0:
            if not (c % 3 == 0 or c % 5 == 0):
                print('DENIED')
                return
    print('APPROVED')
if __name__ == '__main__':
    main()
