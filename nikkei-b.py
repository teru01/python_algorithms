import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
from collections import Counter


def main():
    n = int(input().strip())
    d = list(map(int, input().strip().split()))
    if d[0] != 0:
        print(0)
        return
    e = sorted(list(set(d)))
    for i, v in enumerate(e):
        if i != v:
            print(0)
            return
    v = dict(Counter(d))
    if v[0] != 1:
        print(0)
        return
    i = 0
    ans = 1
    while True:
        if i in v:
            if i == 0:
                i += 1
                continue
            ans *= v[i-1] ** v[i]
            ans %= 998244353
        else:
            break
        i += 1
    print(ans)

if __name__ == '__main__':
    main()
