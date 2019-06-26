import sys
input = sys.stdin.readline

def can_reach(s, p, q):
	for i in range(p, q):
		if s[i] == '#' and s[i+1] == '#':
			return False
	return True

def main():
	_, a, b, c, d = map(lambda i: int(i)-1, input().strip().split())
	s = input().strip()
	if a < c < b < d:
		if can_reach(s, a, c) and can_reach(s, b, d):
			print('Yes')
		else:
			print('No')
	elif a < b < c < d:
		if can_reach(s, a, c) and can_reach(s, b, d):
			print('Yes')
		else:
			print('No')
	else:
		if can_reach(s, a, c) and can_reach(s, b, d):
			for i in range(b-1, d):
				if s[i] == '.' and s[i+1] == '.' and s[i+2] == '.':
					print('Yes')
					return
		print('No')

if __name__ == '__main__':
	main()
