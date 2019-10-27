import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    n = int(input().strip())
    S = input().strip()
    stack = []
    ans = 0
    for c in S:
        if c == '#':
            stack.append('#')
        else:
            if len(stack) != 0:
                stack.pop()
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
