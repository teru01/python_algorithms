import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    t = 0
    kind = set()
    for e in v:
        if e // 400 >= 8:
            t += 1
        else:
            kind.add(e // 400)
    print(max(1,len(kind)), len(kind) + t)

if __name__ == '__main__':
    main()
