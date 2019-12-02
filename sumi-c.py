import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    a = (n % 100) // 10
    b = (n % 10)
    # if a == b == 0:
    #     print(1)
    #     return
    if b == 0:
        k = 0
    elif 1 <= b <= 5:
        k = 1
    else:
        k = 2
    s = a * 2 + k
    # print(s, a, b)
    if s <= n / 100:
        print(1)
    else:
        print(0)



if __name__ == '__main__':
    main()
