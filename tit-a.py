import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	a, b, t = map(int, input().strip().split())
	span = b - a
	print(b + ((t - b + span - 1) // span) * span)
if __name__ == '__main__':
	main()
