import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from bisect import bisect_left

def lis(a, n):
    l = [a[0]]
    for i in range(n):
        if l[-1] < a[i]:
            l.append(a[i])
        else:
            q = bisect_left(l, a[i])
            l[q] = a[i]
    return len(l)

def main():
    n = int(input().strip())
    a = [0] * (n)
    for i in range(0, n):
        a[i] = int(input().strip())
    print(lis(a, n))


if __name__ == '__main__':
    main()
