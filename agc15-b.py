import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    s = input().strip()
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == 'U':
            ans += n - i - 1
            ans += 2 * i
        else:
            ans += i
            ans += 2 * (n-i-1)
    print(ans)


if __name__ == '__main__':
    main()
