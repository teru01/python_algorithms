import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from collections import deque
from copy import deepcopy

def is_ok(state, n):
    templ = [i for i in range(1, n)] + [0]
    for i in range(3):
        for j in range(3):
            if state[i][j] != templ[i*3+j]:
                return False
    return True

def pos_zero(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return (i, j)

def s_swap(s, i, j, k, l):
    d = deepcopy(s)
    d[i][j], d[k][l] = d[k][l], d[i][j]
    return d

def main():
    state = [[0] * 3 for _ in range(3)]
    for i in range(3):
        state[i] = list(map(int, input().strip().split()))
    q = deque()
    q.append((state, 0, -1, -1))
    while len(q) != 0:
        s, a, pre_i, pre_j = q.popleft()
        if is_ok(s, 9):
            print(a)
            return
        i, j = pos_zero(s)
        # print("=================")
        # for x in range(3):
        #     print(s[x])
        # print(i, j)
        if i != 0 and i-1 != pre_i:
            q.append((s_swap(s, i, j, i-1, j), a+1, i, j))
        if i != 2 and i+1 != pre_i:
            q.append((s_swap(s, i, j, i+1, j), a+1, i, j))
        if j != 0 and j-1 != pre_j:
            q.append((s_swap(s, i, j, i, j-1), a+1, i, j))
        if j != 2 and j+1 != pre_j:
            q.append((s_swap(s, i, j, i, j+1), a+1, i, j))


if __name__ == '__main__':
    main()
