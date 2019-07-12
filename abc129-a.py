import sys
input = sys.stdin.readline

def main():
	v = list(map(int, input().strip().split()))
	v.sort()
	print(v[0]+v[1])

if __name__ == '__main__':
	main()
