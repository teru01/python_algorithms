import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    s = input().strip()
    stack = []
    for c in s:
        if c == 'S':
            stack.append('S')
        else:
            if len(stack) > 0 and stack[-1] == 'S':
                stack.pop()
            else:
                stack.append('T')
    print(len(stack))

if __name__ == '__main__':
    main()
