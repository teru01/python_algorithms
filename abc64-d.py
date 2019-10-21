import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
from collections import deque

def main():
    n = int(input().strip())
    S = input().strip()
    s = deque(S)
    st = []
    for c in S:
        if c == ')':
            if len(st) == 0:
                s.appendleft('(')
            else:
                st.pop()
        else:
            st.append('(')
    s.append(')' * len(st))
    print(''.join(s))

if __name__ == '__main__':
    main()
