import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def one_ichigo(a, b, c, d):
    return True

def rec(l, r, t, b, mat):
    if one_ichigo(l, r, t, b):
        
        return
    else:
        rec(l, r-1, t, b, mat)
        rec(r, )

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    

if __name__ == '__main__':
    main()
