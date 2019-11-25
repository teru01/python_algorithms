import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
import string

def main():
    n = int(input().strip())
    v = input().strip()
    newv = [0] * (len(v))
    al = string.ascii_uppercase
    for i, c in enumerate(v):
        newv[i] = al[(al.index(c) + n) % len(al)]
    print("".join(newv))

if __name__ == '__main__':
    main()
