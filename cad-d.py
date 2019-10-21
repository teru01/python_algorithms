import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    n = int(input().strip())
    a = [0] * n
    for i in range(n):
        a[i] = int(input().strip())
    if all(True if v % 2 == 0 else False for v in a):
        print('second')
    else:
        print('first')

if __name__ == '__main__':
    main()
