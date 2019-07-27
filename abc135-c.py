import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	a = list(map(int, input().strip().split()))
	b = list(map(int, input().strip().split()))
	s = 0
	for i in range(n):
		if a[i] < b[i]:
			s += a[i]
			if b[i] - a[i] < a[i+1]:
				a[i+1] -= (b[i] - a[i])
				s += b[i] - a[i]
			else:
				s += a[i+1]
				a[i+1] = 0
		else:
			s += b[i]
	print(s)

if __name__ == '__main__':
	main()
