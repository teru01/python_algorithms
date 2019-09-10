import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	n = int(input().strip())
	v = input().strip()
	if n >= 3200:
		print(v)
	else:
		print("red")

if __name__ == '__main__':
	main()
