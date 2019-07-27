import sys
input = sys.stdin.readline
def main():
	n, k = map(int, input().strip().split())
	v = list(map(int, input().strip().split()))
	ans = 0
	for a in range(k+1):
		for b in range(k-a+1):
			if a + b > n:
				continue
			t = sorted(v[:a] + v[n-b:])
			for i in range(k-a-b):
				if i < len(t) and t[i] < 0:
					t[i] = 0
			ans = max(ans, sum(t))
	print(ans)
if __name__ == '__main__':
	main()
