import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
fl = [0] * (10**5+2)

def main():
    n = int(input().strip())
    ans = 0
    for i in range(n):
        p = int(input().strip())
        if fl[p] == 1:
            ans += 1
        fl[p] = 1
    print(ans)


if __name__ == '__main__':
    main()
