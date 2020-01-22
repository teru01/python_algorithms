import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    a, b = input().strip().split()
    print(sorted([a*int(b), b*int(a)])[0])

if __name__ == '__main__':
    main()
