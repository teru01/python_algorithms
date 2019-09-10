import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	a, b = map(int, input().strip().split())
	if b == 1:
		print(0)
		return
	ans = 1
	kuchi = a
	while kuchi < b:
		ans += 1
		kuchi += a-1
	print(ans)

if __name__ == '__main__':
	main()
