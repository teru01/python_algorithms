import sys
input = sys.stdin.readline

def main():
	n, d = map(int, input().strip().split())
	p = n / (2*d+1)
	if p == int(p):
		print(int(p))
		return
	print(int(p+1))

if __name__ == '__main__':
	main()
