import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    n = int(input().strip())
    for i in range(50000):
        if int(i * 1.08) == n:
            print(i)
            return 0
    print(":(")
    

if __name__ == '__main__':
    main()
