import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from collections import Counter

def main():
    n = int(input().strip())
    v = []
    for i in range(n):
        v.append(input().strip())
    v2 = dict(Counter(v))
    q = []
    for k, w in v2.items():
        q.append([k, w])
    q = sorted(q, key=itemgetter(1), reverse=True)
    # print(q)
    ans = []
    ans.append(q[0][0])
    prev = q[0][1]
    for t in q[1:]:
        if t[1] == prev:
            ans.append(t[0])
    ans = sorted(ans)
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()
