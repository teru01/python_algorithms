import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	a = [0] * n
	for i in range(n):
		a[i] = int(input().strip())
	l = [0] *(n+1)
	r = [0] *(n+1)
	for i in range(0, n):
		l[i+1] = max(l[i], a[i])
	for i in reversed(range(1, n)):
		r[i-1] = max(r[i], a[i])
	for i in range(n):
		print(max(l[i], r[i]))

if __name__ == '__main__':
	main()
