import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    s = [0] * n
    for i in range(n):
        s[i] = input().strip()[::-1]
    s.sort()
    for i in range(n):
        s[i] = s[i][::-1]
        print(s[i])

if __name__ == '__main__':
    main()
