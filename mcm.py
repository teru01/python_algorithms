import sys
input = sys.stdin.readline
a = []

#l <= x < rまでの行列せきの最小値
def rec(l, r):
	if l+1 == r:
		return 0
	if l+2 == r:
		return a[l][0] * a[l][1] * a[l+1][1]
	m = 100000000
	for i in range(l+1, r):
		m = min(m, rec(l, i) + rec(i, r) + a[l][0] * a[i][0] * a[r-1][1])
	return m

def main():
	global a
	n = int(input().strip())
	for i in range(n):
		a.append(tuple(map(int, input().strip().split())))

	print(rec(0, n))

if __name__ == '__main__':
	main()
