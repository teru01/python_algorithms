import sys
input = sys.stdin.readline

def pri(tbl, tbl2, tbl3, tbl4, n, m):
	for i in range(n):
		for j in range(m):
			print("{:2}".format(tbl[i][j]+tbl2[i][j]+tbl3[i][j]+tbl4[i][j]), end='')
		print('')
	print('')

def main():
	n, m = map(int, input().strip().split())
	v = []
	for i in range(n):
		v.append(input().strip())
	tbl = [[0] * m for _ in range(n)]
	tbl2 = [[0] * m for _ in range(n)]
	tbl3 = [[0] * m for _ in range(n)]
	tbl4 = [[0] * m for _ in range(n)]
	for i in range(n):
		for j in range(m):
			if v[i][j] == '#':
				tbl[i][j] = -1
			elif j == 0:
				continue
			else:
				tbl[i][j] = tbl[i][j-1] + 1
	# pri(tbl, tbl2, tbl3, tbl4, n, m)
	for i in range(n):
		for j in range(m-1, -1, -1):
			if v[i][j] == '#':
				tbl2[i][j] = -1
			elif j == m-1:
				continue
			else:
				tbl2[i][j] = tbl2[i][j+1] + 1
	# pri(tbl, tbl2, tbl3, tbl4, n, m)

	
	for j in range(m):
		for i in range(n):
			if v[i][j] == '#':
				tbl3[i][j] = -1
			elif i == 0:
				continue
			else:
				tbl3[i][j] = tbl3[i-1][j] + 1
	for j in range(m):
		for i in range(n-1, -1, -1):
			if v[i][j] == '#':
				tbl4[i][j] = -1
			elif i == n-1:
				continue
			else:
				tbl4[i][j] = tbl4[i+1][j] + 1
	# for i in range(n):
	# 	print(tbl[i])
	# pri(tbl, tbl2, tbl3, tbl4, n, m)
	ans = 0
	for i in range(n):
		for j in range(m):
			ans = max(ans, tbl[i][j]+tbl2[i][j]+tbl3[i][j]+tbl4[i][j])
	print(ans+1)

if __name__ == '__main__':
	main()
