import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n, k = list(map(int, input().strip().split()))
    d = input().strip().split()
    ans = n
    while True:
        sans = str(ans)
        flag = False
        for c in sans:
            # print(c)
            # print('d ', d)
            if c in d:
                ans += 1
                flag = True
                break
        if flag:
            continue
        print(sans)
        return

    

if __name__ == '__main__':
    main()
