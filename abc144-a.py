import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    a, b = map(int, input().strip().split())
    if a <10 and b < 10:
        print(a*b)
    else:
        print(-1)

if __name__ == '__main__':
    main()
