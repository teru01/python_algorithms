import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

h = 0
w = 0
k = 0
a = []
num = 0
cnt = []
c = []

def main():
    global h, w, k, a, num, cnt, c
    h, w, k = list(map(int, input().strip().split()))
    c = [[0] * w for _ in range(h)]
    a = [[0] * w for _ in range(h)]
    cnt = [0] * h
    for i in range(h):
        c[i] = input().strip()
        cnt[i] = sum(1 if v == '#' else 0 for v in c[i])

    v = []
    for i in range(h):
        if cnt[i] >= 1:
            v.append(i)
    for i in range(len(v)):
        if i == 0:
            cl = 0
        else:
            cl = v[i-1]+1
        if i == len(v)-1:
            cr = h-1
        else:
            cr = v[i]
        solve(cl, cr)
    for i in range(h):
        print(" ".join(str(c) for c in a[i]))

def solve(cl, cr):
    global a, num
    p = []
    for i in range(cl, cr+1):
        for j in range(w):
            if c[i][j]== '#':
                p.append(j)
    p.sort()
    for i in range(len(p)):
        if i == 0:
            vl = 0
        else:
            vl = p[i-1]+1
        if i == len(p)-1:
            vr = w-1
        else:
            vr = p[i]
        num += 1

        for j in range(cl, cr+1):
            for k in range(vl, vr+1):
                a[j][k] = num

if __name__ == '__main__':
    main()
