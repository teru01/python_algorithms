import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	a = [0] * n
	for i in range(n):
		a[i] = int(input().strip())
	b = sorted(a, reverse=True)
	first = b[0]
	second = b[1]
	for i in range(n):
		if a[i] == first:
			print(second)
		else:
			print(first)

if __name__ == '__main__':
	main()
