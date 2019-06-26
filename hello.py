import sys
input = sys.stdin.readline

a = int(input().strip())
b, c = list(map(int, input().strip().split()))
s = input().strip()
print("{} {}".format(a+b+c, s))
