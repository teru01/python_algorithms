import sys
input = sys.stdin.readline

def main():
	n, k = map(int, input().strip().split())
	h = [0] * n
	for i in range(n):
		h[i] = int(input().strip())
	H = sorted(h)
	print(min(H[i] - H[i-k+1] for i in range(k-1, n)))
	# ans = 10**9
	# for i in range(n-k+1):
	# 	ans = min(ans, H[i+k-1]-H[i])
	# print(ans)


if __name__ == '__main__':
	main()
