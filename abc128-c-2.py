import sys
input = sys.stdin.readline

def main():
	n, m = map(int, input().strip().split())
	A = [0] * n
	for i in range(m):
		sw = list(map(int, input().strip().split()))[1:]
		for e in sw:
			e -= 1
			A[e] |= 1 << i

	pl = list(map(int, input().strip().split()))
	p = 0
	for i, e in enumerate(pl):
		p = p << 1
		p += e

	j = 0
	ans = 0
	while j < (1 << n):
		t = 0
		for i in range(n):
			if j >> i & 1:
				t ^= A[i]
		if t == p:
			ans += 1
		j += 1

	print(ans)

if __name__ == '__main__':
	main()
