import sys
input = sys.stdin.readline

def main():
	v = list(map(int, input().strip().split(',')))
	n = len(v)
	ans = []
	for i in range(1, n):
		if i % 2 != 0 or v[i-1] == v[i]:
			ans.append(str(v[i]))
	print(",".join(ans))

if __name__ == '__main__':
	main()
