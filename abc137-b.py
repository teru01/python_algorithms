import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	k, x = map(int, input().strip().split())
	for i in range(x-k+1, x+k):
		print("{} ".format(i), end="")
	print("")

if __name__ == '__main__':
	main()
