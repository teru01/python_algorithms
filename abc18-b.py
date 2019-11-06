import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    s = input().strip()
    n = int(input().strip())
    m = len(s)
    s2 = [0] * m
    s3 = [0] * m
    for k in range(m):
        s2[k] = s[k]
    for i in range(n):
        l, r = map(int, input().strip().split())
        for k in range(m):
            s3[k] = s2[k]
        for j in range(l-1, r):
            s2[j] = s3[r-1-(j-(l-1))]
    print("".join(s2))
if __name__ == '__main__':
    main()
