import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	a = list(map(int, input().strip().split()))
	b = list(map(int, input().strip().split()))
	s = 0
	for i in range(n):
		l = min(a[i], b[i])
		a[i] -= l
		b[i] -= l
		r = min(a[i+1], b[i])
		a[i+1] -= r
		b[i] -= r
		s += l + r
	print(s)

if __name__ == '__main__':
	main()
