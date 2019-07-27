import sys
input = sys.stdin.readline

def main():
	n, k = map(int, input().strip().split())
	a = list(map(int, input().strip().split()))
	s = 0
	i = 0
	ans = 0
	for j in range(n):
		s += a[j]
		if s >= k:
			ans += n-j
			while True:
				s -= a[i]
				i += 1
				if s >= k:
					ans += n-j
				else:
					break

	print(ans)
if __name__ == '__main__':
	main()
