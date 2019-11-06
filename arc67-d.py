import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    n, a, b = map(int, input().strip().split())
    x = list(map(int, input().strip().split()))
    ans = 0
    for i in range(1, n):
        ans += min((x[i] - x[i-1]) * a, b)
    print(ans)
if __name__ == '__main__':
    main()
