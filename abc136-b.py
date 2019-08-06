import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	c = 0
	for i in range(1, n+1):
		if len(str(i)) % 2 == 1:
			c += 1
	print(c)
if __name__ == '__main__':
	main()
