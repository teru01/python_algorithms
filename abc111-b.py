import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	d = (n + 111 - 1) //111
	print(111 * d)

if __name__ == '__main__':
	main()
