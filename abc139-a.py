import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	v = input().strip()
	v2 = input().strip()
	ans = 0
	for i in range(3):
		if v[i] == v2[i]:
			ans += 1
	print(ans)

if __name__ == '__main__':
	main()
