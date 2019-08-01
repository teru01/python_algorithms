import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	a = list(map(int, (input().strip().split())))
	l = [0] *(n+1)
	r = [0] *(n+1)
	for i in range(0, n):
		l[i+1] = l[i] + a[i]
	for i in reversed(range(0, n)):
		r[i] = r[i+1] + a[i]
	for i in range(n+1):
		print(l[i])
	print("===========")
	for i in reversed(range(-1, n)):
		print(r[i+1])

if __name__ == '__main__':
	main()
