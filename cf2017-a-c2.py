import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
from collections import defaultdict, Counter

def main():
    h, w = map(int, input().strip().split())
    mat = [0] * h
    d = {}
    for i in range(h):
        s = input().strip()
        for k, v in dict(Counter(s)).items():
            if k in d:
                d[k] += v
            else:
                d[k] = v
    num = [0] * 4
    for k, v in d.items():
        num[v % 4] += 1

    ans = "No"
    if h % 2 == 1 and w % 2 == 1:
        if num[1] + num[3] == 1 and num[2] <= h // 2 + w // 2:
            ans = "Yes"
    elif h % 2 == 1:
        if num[1] + num[3] == 0 and num[2] <= w // 2:
            ans = "Yes"
    elif w % 2 == 1:
        if num[1] + num[3] == 0 and num[2] <= h // 2:
            ans = "Yes"
    else:
        if num[1] + num[3] + num[2] == 0:
            ans = 'Yes'
    print(ans)
    # print(num)
if __name__ == '__main__':
    main()
