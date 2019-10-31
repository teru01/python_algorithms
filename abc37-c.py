import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    b = [0] * (n+1)
    for i in range(1, n+1):
        b[i] = b[i-1] + a[i-1]
    ans = 0
    for i in range(n-k+1):
        # print(b[i+k] - b[i])
        ans += b[i+k] - b[i]
    print(ans)
if __name__ == '__main__':
    main()
