import sys
input = sys.stdin.readline

def main():
	a, b, c = map(int, input().strip().split())
	d = c-a+b
	if d < 0:
		print(0)
	else:
		print(d)

if __name__ == '__main__':
	main()
