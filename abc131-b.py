import sys
input = sys.stdin.readline

def main():
	n, l = map(int, input().strip().split())
	a = [0] * n
	m = 10**9
	u = None
	for i in range(n):
		a[i] = l + i
		if abs(a[i]) < m:
			m = abs(a[i])
			u = i
	print(sum(a) - a[u])

if __name__ == '__main__':
	main()
