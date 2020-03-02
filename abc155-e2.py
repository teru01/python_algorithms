import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    s = reversed(list(input().strip()))
    s += '0'
    n = len(s)
    dp = [[INF] * 2 for _ in range(n+1)]
    

if __name__ == '__main__':
    main()
