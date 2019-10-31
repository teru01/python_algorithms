import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    cnt = 0

    k = sum(max(0, a[i]-b[i]) for i in range(n))
    l = sum(max(0, (b[i] - a[i])//2) for i in range(n))
    if k <= l:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
