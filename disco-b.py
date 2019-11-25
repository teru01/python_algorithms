import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def calc_sum(v, n):
    a = [0] * (n)
    for i in range(n):
        if i == 0:
            a[i] = v[i]
            continue
        a[i] = a[i-1] + v[i]
    return a

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))

    a = calc_sum(v, n)
    b = list(reversed(calc_sum(list(reversed(v)), n)))

    ans = INF
    for i in range(n-1):
        ans = min(ans, abs(a[i] - b[i+1]))
    print(ans)
if __name__ == '__main__':
    main()
