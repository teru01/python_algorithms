import sys
input = sys.stdin.readline

def main():
	n, k = map(int, (input().strip().split()))
	v = list(map(int, input().strip().split()))
	ans = 0
	s = 0
	r = 0
	for l in range(n):
		while(s < k and r < n):
			s += v[r]
			r += 1
		if s < k:
			break
		ans += n - r + 1
		s -= v[l]
	print(ans)

if __name__ == '__main__':
	main()

