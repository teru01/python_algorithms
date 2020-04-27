import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def rec(s, n):
    c = 0
    if s == '':
        s = '0'
    if int(s) > n:
        return 0
    if len(set(s)) == 4:
        # print(s)
        c += 1
    for i in '357':
        w = s + i
        c += rec(w, n)
    return c

def main():
    n = int(input().strip())
    print(rec('', n))

if __name__ == '__main__':
    main()
