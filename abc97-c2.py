import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    s = input().strip()
    k = int(input().strip())
    n = len(s)
    strs = set()
    for i in range(n):
        for j in range(1, k+1):
            strs.add(s[i:min(i+j, n)])
    strs = list(strs)
    # print(sorted(strs))
    print(sorted(strs)[k-1])


if __name__ == '__main__':
    main()
