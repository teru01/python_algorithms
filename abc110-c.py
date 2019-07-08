import sys
input = sys.stdin.readline

def main():
	s = input().strip()
	t = input().strip()
	l = {chr(c): chr(c) for c in range(ord('a'), ord('z')+1)}
	for i, c in enumerate(s):
		if l[c] != c and (l[c] != t[i] or l[t[i]] != c):
			print('No')
			return
		l[c] = t[i]
		l[t[i]] = c
	print('Yes')
	for c in l.items():
		print(c, end='')
	print('')

if __name__ == '__main__':
	main()
