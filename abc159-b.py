import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def is_ok(s):
    return s == ''.join(reversed(s))

def main():
    s = input().strip()
    n = len(s)
    if is_ok(s) and is_ok(s[0:(n-1)//2]) and is_ok(s[(n+3)//2-1:n]):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
