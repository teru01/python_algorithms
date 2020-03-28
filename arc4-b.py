import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

# 17:20
def main():
    n = int(input().strip())
    v = [0] * n
    for i in range(n):
        v[i] = int(input().strip())
    v.sort(reverse=True)
    print(sum(v))
    print(max(0, v[0] - sum(v[1:])))


if __name__ == '__main__':
    main()
