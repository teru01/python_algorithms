import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
import string

def main():
    s = input().strip()
    n = len(s)
    m = {}
    for c in string.ascii_lowercase:
        t = list(s[:])
        count = 0
        while True:
            if len(set(t)) == 1:
                m[c] = count
                break
            for i in range(len(t) - 1):
                if t[i] == c or t[i+1] == c:
                    t[i] = c
            t = t[:len(t) - 1]
            count += 1
    print(min(m.values()))

if __name__ == '__main__':
    main()
