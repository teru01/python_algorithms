import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    s = input().strip()
    if s[:2] == 'SU':
        print(7)
    elif s[:2] == 'MO':
        print(6)
    elif s[:2] == 'TU':
        print(5)
    elif s[:2] == 'WE':
        print(4)
    elif s[:2] == 'TH':
        print(3)
    elif s[:2] == 'FR':
        print(2)
    elif s[:2] == 'SA':
        print(1)

if __name__ == '__main__':
    main()
