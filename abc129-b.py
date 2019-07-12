import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	v = list(map(int, input().strip().split()))
	ans = 1000000000000000
	for i in range(1, n):
		s1 = sum(v[:i+1])
		s2 = sum(v[i+1:])
		ans = min(abs(s1-s2), ans)
	print(ans)
if __name__ == '__main__':
	main()
