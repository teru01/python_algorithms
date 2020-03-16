import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n, d, k = list(map(int, input().strip().split()))
    l = [0] * d
    r = [0] * d
    s = [0] * k
    t = [0] * k
    for i in range(d):
        l[i], r[i] = list(map(int, input().strip().split()))
    for i in range(k):
        s[i], t[i] = list(map(int, input().strip().split()))
    for i in range(k):
        days = 0
        while s[i] != t[i]:
            if l[days] <= s[i] <= r[days]:
                if l[days] <= t[i] <= r[days]:
                    s[i] = t[i]
                elif s[i] < t[i]:
                    s[i] = r[days]
                else:
                    s[i] = l[days]
            days += 1
        print(days)


if __name__ == '__main__':
    main()
