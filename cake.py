import sys
input = sys.stdin.readline
from operator import itemgetter
from random import random

def main():
    n = int(sys.argv[1])
    var = [0] * 10
    avr = 0
    for _ in range(n):
        r1 = random()
        r2 = random()
        if r1 > r2:
            r1, r2 = r2, r1
        var[int((r2 - r1) * 10)] += 1
        avr += r2 - r1
    for i, c in enumerate(reversed(var)):
        percent = c / n * 100
        graph = "*" * int(percent)
        print("{:2d}% <= {} ({:.2f}%)".format((9 - i) * 10, graph, percent))
    print("avr: {:.2f}".format(avr / n))


if __name__ == '__main__':
    main()
