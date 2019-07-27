import sys
input = sys.stdin.readline

def main():
	n, q = map(int, (input().strip().split()))
	a = list(map(int, input().strip().split()))
	x = list(map(int, input().strip().split()))
	for i in range(q):
		r = 0
		k = x[i]
		s = 0
		ans = 0
		for l in range(n):
			while(r < n and s + a[r] <= k):
				s += a[r]
				r += 1
			# print(r)
			ans += r - l
			# print(r - l)
			s -= a[l]
		print(ans)

if __name__ == '__main__':
	main()
