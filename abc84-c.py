import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    c = [0] * (n - 1)
    s = [0] * (n - 1)
    f = [0] * (n - 1)
    for i in range(n-1):
        c[i], s[i], f[i] = list(map(int, input().strip().split()))
    for k in range(n-1):
        t = 0
        for i in range(k, n-1):
            if t < s[i]:
                # ans += s[i] - t
                t = s[i]
            else:
                # ans += f[i] - (t - s[i]) % f[i]
                t = f[i] * ((t + f[i] - 1) // f[i])

            # ans += c[i]
            t += c[i]
        print(t)
    print(0)



if __name__ == '__main__':
    main()
