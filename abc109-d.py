import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	h, w = map(int, input().strip().split())
	a = [[] for _ in range(h)]
	for i in range(h):
		a[i] = list(map(int, input().strip().split()))
	ans = []
	for i in range(h-1):
		for j in range(w):
			if a[i][j] % 2 == 1:
				a[i][j] -= 1
				a[i+1][j] += 1
				ans.append((i+1, j+1, i+2, j+1))

	for j in range(w-1):
		if a[h-1][j] % 2 == 1:
			a[h-1][j] -= 1
			a[h-1][j+1] += 1
			ans.append((h, j+1, h, j+2))
	n = len(ans)
	print(n)
	for i in range(n):
		print("{} {} {} {}".format(ans[i][0], ans[i][1], ans[i][2], ans[i][3]))
if __name__ == '__main__':
	main()
