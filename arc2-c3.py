import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    v = input().strip()
    ans = n
    for c in ('A', 'B', 'X', 'Y'):
        for d in ('A', 'B', 'X', 'Y'):
            for e in ('A', 'B', 'X', 'Y'):
                for f in ('A', 'B', 'X', 'Y'):
                    k = 0
                    if n % 2 == 0:
                        i = 1
                        while i < n:
                            if (v[i-1] == c and v[i] == d) or (v[i-1] == e and v[i] == f):
                                k += 1
                                i += 1
                            i += 1
                        ans = min(ans, n-k)
                    else:
                        for i in (1, 2):
                            k = 0
                            while i < n:
                                if (v[i-1] == c and v[i] == d) or (v[i-1] == e and v[i] == f):
                                    k += 1
                                    i += 1
                                i += 1
                            # print(k)
                            ans = min(ans, n-k)
    print(ans)



if __name__ == '__main__':
    main()
