import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    u = input().strip()
    v = input().strip()
    s = u + v

    A = [0] * len(s)
    A[0] = len(s)
    i = 1
    prev = 0
    while i < len(s):
        j = 0
        k = i
        if i +  < prev and :

        while j < len(s) and k < len(s) and s[k] == s[j]:
            k += 1
            j += 1
        A[i] = j
        prev = k
        i += 1
    print(A)

if __name__ == '__main__':
    main()
