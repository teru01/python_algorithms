import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	v = list(map(int, input().strip().split()))
	mini = 10**10
	for i in reversed(range(n)):
		mini = min(mini, v[i])
		if v[i] - mini > 1:
			print('No')
			return
	print('Yes')

if __name__ == '__main__':
	main()
