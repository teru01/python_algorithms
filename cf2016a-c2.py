import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    s = input().strip()
    k = int(input().strip())
    ans = []
    for i, c in enumerate(s):
        if i == len(s)-1:
            ans.append(chr(ord('a') + (ord(c) + k % 26 - ord('a')) % 26))
            break
        d = (ord('z') - ord(c) + 1) % 26
        if d <= k:
            k -= d
            ans.append('a')
        else:
            ans.append(c)
    print(''.join(ans))


if __name__ == '__main__':
    main()
