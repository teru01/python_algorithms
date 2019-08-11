import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	s = input().strip()
	k = int(input().strip())
	ans = "1"
	for i in range(len(s)):
		if s[i] != '1' and i+1 <= k:
			ans = s[i]
			break
	print(ans)

if __name__ == '__main__':
	main()
