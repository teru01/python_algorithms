import sys
input = sys.stdin.readline

def main():
	n, m = map(int, input().strip().split())
	v = [0] * (n+1)
	v[0] = 1
	v[1] = 1
	N = []
	for i in range(m):
		a = int(input().strip())
		N.append(a)
	N.append(-1)
	j = 0
	for i in range(1, n+1):
		if N[j] == i:
			v[i] = 0
			j += 1
		else:
			if i == 1:
				v[i] = 1
			else:
				v[i] = v[i-1] + v[i-2]
	print(v[n] % (10**9+7))

if __name__ == '__main__':
	main()
