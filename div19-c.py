import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    v = []
    ra = 0
    rb = 0
    both = 0
    ans = 0
    for i in range(n):
        s = input().strip()
        for j in range(len(s)-1):
            if s[j] == 'A' and s[j+1] == 'B':
                ans += 1
        if s[0] != 'B' and s[-1] == 'A':
            ra += 1
        elif s[0] == 'B' and s[-1] != 'A':
            rb += 1
        elif s[0] == 'B' and s[-1] == 'A':
            both += 1

    if ra + rb == 0 and both > 0:
        ans += both - 1
    else:
        ans += min(ra+both, rb+both)
    print(ans)

if __name__ == '__main__':
    main()
