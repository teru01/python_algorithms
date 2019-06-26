import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	for _ in range(n):
		x = input().strip()
		y = input().strip()
		p = len(x)
		q = len(y)
		c = [[0]*(q+1) for i in range(p+1)]
		for i in range(1, p+1):
			for j in range(1, q+1):
				if x[i-1] == y[j-1]:
					c[i][j] = c[i-1][j-1] + 1
				else:
					c[i][j] = max(c[i-1][j], c[i][j-1])
		print(c[p][q])

if __name__ == '__main__':
	main()
