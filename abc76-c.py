import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def isEqual(s, t):
    if s == t or t == '?':
        return True
    return False

def main():
    ans = []
    s = input().strip()
    t = input().strip()
    for i in range(len(s) - len(t)+1):
        k = i
        w = i
        flag = True
        for j in range(len(t)):
            if not isEqual(t[j], s[k]):
                flag = False
                break
            k += 1
        if flag:
            q = list(s)
            q[w:w+(len(t))] = t
            q = ''.join(q)
            q = q.replace('?', 'a')
            ans.append(q)
    if len(ans) == 0:
        print('UNRESTORABLE')
    else:
        print(sorted(ans)[0])

if __name__ == '__main__':
    main()
