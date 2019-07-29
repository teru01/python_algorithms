import sys
input = sys.stdin.readline

def main():
	s = input().strip()
	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			print('Bad')
			return
	print('Good')

if __name__ == '__main__':
	main()
