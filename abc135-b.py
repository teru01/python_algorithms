import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	v = list(map(int, input().strip().split()))
	v2 = sorted(v)
	if v == v2:
		print('YES')
		return
	# O(n^3)
	for i in range(n-1):
		for j in range(i+1, n):
			w = v[:]
			w[i], w[j] = w[j], w[i]
			if w == v2:
				print('YES')
				return
	print('NO')

if __name__ == '__main__':
	main()
