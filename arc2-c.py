import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from collections import Counter

def make_com(s):
    l = []
    for i in range(len(s)):
        if i % 2== 1:
            l.append(str(s[i-1:i+1]))
    return dict(Counter(l))

def main():
    n = int(input().strip())
    s = input().strip()
    r1 = make_com(s)
    r2 = {}
    if n != 1:
        r2 = make_com(s[1:])
    rl1 = sorted(r1.values(), reverse=True)
    print(r1)
    print(r2)
    # print(rl1)
    ans1 = n
    for i, v in enumerate(rl1):
        if i == 1:
            q = max(v, rl1[0]//2)
            ans1 -= q
        else:
            ans1 -= v
        if i == 1:
            break
    rl2 = sorted(r2.values(), reverse=True)
    # print(rl2)
    ans2 = n
    for i, v in enumerate(rl2):
        if i == 1:
            q = max(v, rl2[0]//2)
            ans2 -= q
        else:
            ans2 -= v
        if i == 1:
            break
    print(min(ans1, ans2))
if __name__ == '__main__':
    main()
