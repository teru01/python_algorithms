import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    x, y = map(int, input().strip().split())
    ans = 0
    for i in [x, y]:
        if i == 3:
            ans += 100000
        elif i == 2:
            ans += 200000
        elif i == 1:
            ans += 300000
    if x == 1 and y == 1:
        ans += 400000
    print(ans)

if __name__ == '__main__':
    main()
