import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    s = input().strip()
    ans = 0
    q = s.split('+')
    for st in q:
        if '0' not in st:
            ans += 1
    print(ans)
    # s += '+'
    # i = 0
    # n = len(s)
    # ans = 0
    # pc = 0
    # c = 0
    # zc = 0
    # while i < n:
    #     if '0' < s[i] <= '9':
    #         c += 1
    #     elif s[i] == '0':
    #         zc += 1
    #     elif s[i] == '*':
    #         pc += 1
    #     elif s[i] == '+':
    #         if zc == 0:
    #             ans += c - pc
    #         pc = 0
    #         zc = 0
    #         c = 0
    #     i += 1
    # print(max(ans, 0))

if __name__ == '__main__':
    main()
