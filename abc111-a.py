import sys
input = sys.stdin.readline

def main():
	s = input().strip()
	for c in s:
		if c == '1':
			print('9', end='')
		elif c == '9':
			print('1', end='')
		else:
			print(c, end='')
	print('')
if __name__ == '__main__':
	main()
