import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	a = []
	a.append(0)
	a.extend(list(map(int, input().strip().split())))
	s = [0] * (n+1)
	for i in reversed(range(1, n+1)):
		j = 1
		d = 0
		while i * j <= n:
			d += s[i*j]
			j += 1
		s[i] = (d+a[i]) % 2
	M = sum(s)
	print(M)
	for i in range(n+1):
		if s[i] == 1:
			print("{} ".format(i), end="")
	print("")

if __name__ == '__main__':
	main()
