import sys
input = sys.stdin.readline
from operator import itemgetter
import heapq

def main():
    n, m = list(map(int, input().strip().split()))
    v = list(map(lambda x: -x, map(int, input().strip().split())))
    q = []
    for item in v:
        heapq.heappush(q, item)
    for _ in range(m):
        p = heapq.heappop(q)
        # print(p)
        heapq.heappush(q, (p+1) // 2)
    print(-sum(q))

if __name__ == '__main__':
    main()
