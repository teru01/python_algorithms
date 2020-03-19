import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from collections import deque

def main():
    r, c = list(map(int, input().strip().split()))
    sx, sy = list(map(lambda x: x-1, map(int, input().strip().split())))
    gx, gy = list(map(lambda x: x-1, map(int, input().strip().split())))
    M = [[0] * c for _ in range(r)]
    C = [[-1] * c for _ in range(r)]
    for i in range(r):
        M[i] = input().strip()
    q = deque()
    q.append((sx, sy))
    C[sx][sy] = 0
    while len(q) != 0:
        x, y = q.popleft()
        for i, j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            if M[x+i][y+j] == '.' and C[x+i][y+j] == -1:
                C[x+i][y+j] = C[x][y] + 1
                if x+i == gx and y+j == gy:
                    break
                q.append((x+i, y+j))
    print(C[gx][gy])


if __name__ == '__main__':
    main()
