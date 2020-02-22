import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    s = input().strip()
    z = [0] * len(s)
    i = 1
    j = 0
    while i < len(s):
        while i + j < len(s) and s[j] == s[i+j]:
            j += 1
        z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while k < j and k + z[k] < j:
            z[i+k] = z[k]
            k += 1
        i += k
        j -= k

if __name__ == '__main__':
    main()
