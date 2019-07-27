import sys
input = sys.stdin.readline

def main():
	n, x = map(int, input().strip().split())
	L = list(map(int, input().strip().split()))
	i = 0
	c = 1
	for l in L:
		i += l
		if i > x:
			break
		c += 1
	print(c)

if __name__ == '__main__':
	main()
