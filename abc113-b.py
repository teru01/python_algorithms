import sys
input = sys.stdin.readline

def main():
	w = 0.006
	n = int(input().strip())
	t, a = map(int, input().strip().split())
	v = list(map(int, input().strip().split()))
	T = 10**9
	ans = 0
	for i in range(n):
		if abs(a - (t-v[i]*w)) < T:
			T = abs(a - (t-v[i]*w))
			ans = i
	print(ans+1)

if __name__ == '__main__':
	main()
