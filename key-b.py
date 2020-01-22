import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    x = [[0, 0] for  _ in range(n)]
    for i in range(n):
        p, q = list(map(int, input().strip().split()))
        x[i][0] = p-q
        x[i][1] = p+q
    x = sorted(x, key=itemgetter(1))
    m = x[0][1]
    ans = 1
    for mi, ma in x[1:]:
        if m <= mi:
            m = ma
            ans += 1

    # x = sorted(x, key=itemgetter(0))
    # M = x[0][0]
    # ans2 = 1
    # print('x: ', x)
    # for mi, ma in x[1:]:

    #     if M >= ma:
    #         print(M, mi, ma)
    #         M = mi
    #         ans2 += 1
    # print(ans, ans2)
    # print(max(ans, ans2))

    print(ans)

if __name__ == '__main__':
    main()
