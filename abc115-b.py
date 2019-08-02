import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	s = [int(input().strip()) for i in range(n)]
	print(sum(s) - max(s) // 2)

if __name__ == '__main__':
	main()
