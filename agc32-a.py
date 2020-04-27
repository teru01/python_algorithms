import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
def main():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))
    ans = []
    while len(v) > 0:
        flag = False
        for j in reversed(range(len(v))):
            # print(j)
            if j+1 == v[j]:
                ans.append(v[j])
                del v[j]
                flag = True
                break
        if not flag:
            print(-1)
            return
    for c in reversed(ans):
        print(c)

if __name__ == '__main__':
    main()
