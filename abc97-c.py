import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
import heapq

def main():
    s = input().strip()
    n = len(s)
    stq = set()
    k = int(input().strip())
    for i in range(n):
        for j in range(i+1, min(i+1+k+1, n+1)):
            stq.add(s[i:j])
    stq = list(stq)
    heapq.heapify(stq)
    for i in range(k):
        ans = heapq.heappop(stq)
        if i == k-1:
            print(ans)

if __name__ == '__main__':
    main()
