import sys
input = sys.stdin.readline

def main():
	n, a, b = map(int, input().strip().split())
	tra = n * a
	tax = b
	print(min(tra, tax))

if __name__ == '__main__':
	main()
