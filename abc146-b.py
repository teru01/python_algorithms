import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
import string

def main():
    n = int(input().strip())
    v = input().strip()
    s = ''
    for c in v:
        ind = ord(c) - ord('A') + n
        ind %= 26
        s += chr(ord('A') + ind)
    print(s)

if __name__ == '__main__':
    main()
