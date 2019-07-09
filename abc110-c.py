import sys
input = sys.stdin.readline

def main():
	s = input().strip()
	t = input().strip()
	l = [-1] * 26
	k = [-1] * 26
	a = ord('a')
	for i in range(len(s)):
		if l[ord(s[i]) - a] != -1 or k[ord(t[i]) - a] != -1:
			if l[ord(s[i]) - a] != t[i] or k[ord(t[i]) - a] != s[i]:
				print('No')
				return
		l[ord(s[i]) - a] = t[i]
		k[ord(t[i]) - a] = s[i]
	print('Yes')


if __name__ == '__main__':
	main()
