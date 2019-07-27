import sys
input = sys.stdin.readline

def main():
	x, a = map(int, input().strip().split())
	if x < a:
		print(0)
	else:
		print(10)

if __name__ == '__main__':
	main()
