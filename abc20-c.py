import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

chars = "abc"
def rec(s, N):
    if len(s) == N:
        print("".join(s))
        return
    for c in chars:
        rec(s + [c], N)

def main():
    n = int(input().strip())
    rec([], n)

if __name__ == '__main__':
    main()
