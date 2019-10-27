import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    s = sum(a)
    if s % n != 0:
        print(-1)
        return
    k = s // n
    b = [k] * n
    c = [a[i] - b[i] for i in range(n)]
    cn = 0
    tmp = 0
    for v in c:
        tmp += v
        if tmp == 0:
            cn += 1
    print(n - cn)
if __name__ == '__main__':
    main()
