import sys
input = sys.stdin.readline

def main():
	S = input().strip()
	n = len(S)
	ans = [0] * n
	for _ in range(2):
		cnt = 0
		for i in range(n):
			if S[i] == 'R':
				cnt += 1
			else:
				ans[i] += cnt // 2
				ans[i-1] += (cnt + 1) // 2
				cnt = 0
		ans = ans[::-1]
		S = S[::-1]
		S = ['R' if S[i] == 'L' else 'L' for i in range(n)]

	for i in range(n):
		print("{} ".format(ans[i]), end="")
	print("")
if __name__ == '__main__':
	main()
