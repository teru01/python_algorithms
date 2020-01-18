import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    if n == 0:
        print(0)
        return
    ans = ''
    c = 0
    while n != 1:
        c += 1
        s, a = divmod(n, -2)
        # print(s, a)
        if a == -1:
            s += 1
            a = 1
        ans += str(a)
        n = s
    ans += '1'
    print(''.join(reversed(ans)))

if __name__ == '__main__':
    main()
