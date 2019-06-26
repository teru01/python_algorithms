import sys
input = sys.stdin.readline

def countingsort(A, B, k):
	C = [0] * (k+1)
	# n = len(A)
	for va in A:
		C[va] += 1

	# 以下2つのループ分でO(n+k)
	for i in range(1, k+1):
		C[i] = C[i-1] + C[i]
	for v in reversed(A):
		B[C[v]] = v
		C[v] -= 1


def main():
	n = int(input().strip())
	v = list(map(int, input().strip().split()))
	B = [0] * (n+1)
	countingsort(v, B, 10000)
	for i in range(1, n+1):
		if i != 1:
			print(" ", end="")
		print(B[i], end="")
		if i == n:
			print("\n", end="")

if __name__ == '__main__':
	main()
