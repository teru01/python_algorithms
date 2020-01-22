import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    m = INF
    ans = 0
    for i in range(n):
        if m >= v[i]:
            ans += 1
            m = v[i]
    print(ans)



if __name__ == '__main__':
    main()
