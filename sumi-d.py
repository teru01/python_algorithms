import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from collections import Counter
from math import factorial

def main():
    n = int(input().strip())
    s = input().strip()
    s += 'E'
    ans = 0
    for i in range(1000):
        a = i // 100
        b = (i % 100) // 10
        c = i % 10
        k = s.find(str(a))
        l = s.find(str(b), k+1)
        m = s.find(str(c), l+1)
        if k != -1 and l != -1 and m != -1:
            # print(a, b, c)
            ans += 1
    print(ans)
    

if __name__ == '__main__':
    main()
