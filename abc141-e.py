import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
    n = int(input().strip())
    s = input().strip()
    ans = 0
    for i in range(len(s)):
        c = 0
        s_i = i
        s_j = i+1
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                if s_i + c == s_j:
                    continue
                if c == 0:
                    s_i = i
                    s_j = j
                i += 1
                c += 1
            else:
                c = 0
            ans = max(ans, c)
    print(ans)

if __name__ == '__main__':
    main()
