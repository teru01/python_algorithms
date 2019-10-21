import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    s = input().strip()
    s = s.replace("BC", "D")
    ac = 0
    ans = 0
    
    for i in range(len(s)):
        if s[i] == 'A':
            ac += 1
        elif s[i] == 'D':
            ans += ac
        else:
            ac = 0
    print(ans)

if __name__ == '__main__':
    main()
