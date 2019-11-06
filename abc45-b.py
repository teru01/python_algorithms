import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)

def main():
    sa = input().strip()
    sb = input().strip()
    sc = input().strip()
    i, j, k = 0, 0, 0
    turn = 'a'
    ans = ''
    while True:
        if turn == 'a':
            if i == len(sa):
                ans = 'A'
                break
            turn = sa[i]
            i += 1
        elif turn == 'b':
            if j == len(sb):
                ans = 'B'
                break
            turn = sb[j]
            j += 1
        else:
            if k == len(sc):
                ans = 'C'
                break
            turn = sc[k]
            k += 1
    print(ans)


if __name__ == '__main__':
    main()
