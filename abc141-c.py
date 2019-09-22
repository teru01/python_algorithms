import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
    n, k, q = map(int, input().strip().split())
    d = [0] * n
    for _ in range(q):
        i = int(input().strip()) - 1
        d[i] += 1
    for c in d:
        if k - q + c > 0:
            print('Yes')
        else:
            print('No')
            
if __name__ == '__main__':
    main()
