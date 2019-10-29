import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
from math import atan, pi

def main():
    a, b, x = map(int, input().strip().split())
    if x > a **2 * b / 2:
        print(atan(2 * (a**2*b - x)/ a ** 3) * 180/pi)
    else:
        print(90 - atan(2 * x / (a * b ** 2)) * (180 / pi))

if __name__ == '__main__':
    main()
