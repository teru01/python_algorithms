import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

S = "abcdefghijkl"
N = 0
def rec(s):
    if len(s) == N:
        print(''.join(s))
        return
    for i in range(len(set(s))+1):
        s.append(S[i])
        rec(s)
        s.pop()

def main():
    global N
    N = int(input().strip())
    rec([])

if __name__ == '__main__':
    main()
