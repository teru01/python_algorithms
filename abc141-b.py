import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
    v = input().strip()
    for i in range(len(v)):
        if i % 2 == 0:
            if v[i] not in ('R', 'U', 'D'):
                print('No')
                return
        elif i % 2 == 1:
            if v[i] not in ('L', 'U', 'D'):
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()
