import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    s = input().strip()
    ans = list(s[:])
    k = int(input().strip())
    for i in range(len(s)):
        d = (ord('z') - ord(s[i]) + 1) % 26
        if k - d >= 0:
            ans[i] = 'a'
            k -= d
        if i == len(s) - 1:
            # print((ord(ans[i]) + k%26) % 26)
            ans[i] = chr(ord('a') + (ord(ans[i]) - ord('a') + k%26) % 26)
    print(''.join(ans))

if __name__ == '__main__':
    main()
