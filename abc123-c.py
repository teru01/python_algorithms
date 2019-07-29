import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	s = [0] * 5
	for i in range(5):
		s[i] = int(input().strip())
	m = min(s)
	if n % m == 0:
		print(n // m + 4)
	else:
		print(n // m + 5)

if __name__ == '__main__':
	main()
