import sys
input = sys.stdin.readline

def main():
	a, p = map(int, input().strip().split())
	print((3 * a + p) // 2)

if __name__ == '__main__':
	main()
