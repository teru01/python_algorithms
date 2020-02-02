import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from bisect import bisect_left

def main():
    n = int(input().strip())
    a = [0] * n
    for i in range(n):
        a[i] = int(input().strip())
    l = [a[0]]
    for i in range(1, n):
        if a[i] <= l[-1]:
            k = bisect_left(l, a[i])
            l[k] = a[i]
        else:
            l.append(a[i])
    print(len(l))

if __name__ == '__main__':
    main()
