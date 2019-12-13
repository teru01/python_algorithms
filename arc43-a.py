import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n, a, b = list(map(int, input().strip().split()))
    s = [0] * n
    for i in range(n):
        s[i] = int(input().strip())
    M = max(s)
    m = min(s)
    if M == m:
        print(-1)
        return
    p = b / (M - m)
    avr = sum(s) / n
    q = a - avr*p
    print(p, q)


if __name__ == '__main__':
    main()
