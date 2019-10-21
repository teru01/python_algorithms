import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
from collections import Counter

# def f2(s):
#     n = len(s)
#     c = 0
#     ans = 0
#     for i in range(n-1):
#         if s[i] == s[i+1]:
#             c += 1
#             if i == n-2:
#                 ans += (c+1) // 2
#         else:
#             ans += (c+1) // 2
#             c = 0
#     return ans

def f(s):
    n = len(s)
    i = 0
    ans = 0
    while i < n-1:
        c = 0
        while i < n-1 and s[i] == s[i+1]:
            c += 1
            i += 1
        ans += (c+1) // 2
        i += 1
    return ans

def main():
    s = input().strip()
    k = int(input().strip())
    n = len(s)
    if len(Counter(s)) == 1:
        print(n * k // 2)
        return
    ini = f(s)
    dif = f(s*2) - ini
    print(ini + dif * (k-1))

if __name__ == '__main__':
    main()
