import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def num(w, p, k):
    ans = 0
    kg = 0
    tr = 0
    i = 0
    while i < len(w):
        if kg + w[i] <= p:
            kg += w[i]
            i += 1
        else:
            tr += 1
            if tr >= k:
                break
            kg = 0
    return i

def main():
    n, k = list(map(int, input().strip().split()))
    w = [0] * n
    for i in range(n):
        w[i] = int(input().strip())

    l = 0
    r = INF
    while l + 1 < r:
        m = (l + r) // 2
        s = num(w, m, k)
        # print("s, m: ", s, m)
        if s == n:
            r = m
        else:
            l = m
    print(r)

if __name__ == '__main__':
    main()
