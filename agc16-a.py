import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
from collections import defaultdict

def main():
    s = input().strip()
    n = len(s)
    d = defaultdict(int)
    for i, c in enumerate(s):
        j = s[:i].find(c)
        if j != -1:
            k = i - j + 1
        else:
            k = i
        if i != n-1:
            l = s[i+1:].find(c)
        else:
            l = -1
        if l == -1:
            m = n - i - 1
        else:
            m = l
        print(c, d[c], k, m)
        d[c] = max(d[c], k, m)
    print(d)
    print(min(d.values()))


if __name__ == '__main__':
    main()
