import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

h = 0
w = 0
k = 0
a = []
num = 1
cnt = []
c = []

def rec(x1, y1, x2, y2):
    global num
    # print("x1:{}, y1:{}, x2:{}, y2:{}".format(x1, y1, x2, y2))
    sts = []
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            if c[i][j] == '#':
                sts.append((j, i)) # x, y
    if len(sts) == 1:
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                a[i][j] = num
        num += 1
        return
    p1, q1 = sts[0]
    p2, q2 = sts[1]
    if q1 < q2:
        rec(x1, y1, x2, q1)
        rec(x1, q1+1, x2, y2)
    else:
        # q1 = q2
        rec(x1, y1, min(p1, p2), y2)
        rec(min(p1, p2)+1, y1, x2, y2)

def main():
    global h, w, k, a, num, cnt, c
    h, w, k = list(map(int, input().strip().split()))
    c = [[0] * w for _ in range(h)]
    a = [[0] * w for _ in range(h)]
    for i in range(h):
        c[i] = input().strip()

    rec(0, 0, w-1, h-1)
    for i in range(h):
        print(" ".join(str(c) for c in a[i]))


if __name__ == '__main__':
    main()
