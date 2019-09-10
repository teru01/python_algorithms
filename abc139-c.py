import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	n = int(input().strip())
	v = list(map(int, input().strip().split()))
	diff = []
	for i in range(n-1):
		diff.append(v[i+1] - v[i])
	ans = 0
	tmp = 0
	for k in diff:
		if k > 0:
			ans = max(ans, tmp)
			tmp = 0
		else:
			tmp += 1
	ans = max(ans, tmp)
	print(ans)

if __name__ == '__main__':
	main()
