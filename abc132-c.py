import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	v = list(map(int, input().strip().split()))
	ans = 0
	if len(v) % 2 == 0:
		t = sorted(v)
		ans = t[n//2] - t[n//2 - 1]
	print(ans)

if __name__ == '__main__':
	main()
