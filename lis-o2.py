import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    a = [0] * (n)
    b = [0] * (n)
    for i in range(n):
        a[i] = int(input().strip())
    for i in range(n):
        b[i] = 1
        for j in range(i):
            if a[j] < a[i]:
                b[i] = max(b[i], b[j]+1)
    print(max(b))

if __name__ == '__main__':
    main()
