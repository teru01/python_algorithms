import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
from collections import deque

def main():
    n = int(input().strip())
    a = [0] * n
    for i in range(n):
        a[i] = int(input().strip())
    a = deque(sorted(a))

    d = deque()
    for i in range(n):
        e = -20
        if i % 2 == 0:
            e = a.popleft()
        else:
            e = a.pop()
        if len(d) > 0:
            if abs(e - d[0]) > abs(e - d[-1]):
                d.appendleft(e)
            else:
                d.append(e)
        else:
            d.append(e)
    ans = 0
    d = list(d)
    for i in range(n-1):
        ans += abs(d[i] - d[i+1])
    print(d)
    print(ans)

if __name__ == '__main__':
    main()
