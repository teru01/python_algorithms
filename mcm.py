import sys
input = sys.stdin.readline
N = 100
def main():
	n = int(input().strip())
	p = [0] * (N+1)
	for i in range(1, n+1):
		p[i-1], p[i] = map(int, input().strip().split())
	m = [[0] * (N+1) for i in range(N+1)]
	for l in range(2, n+1):
		# i, jは対象となる行列の数が2, 3, 4...と増えていくようにする
		# ((M1,M2),M3)などは(M1,M2)が求まっている必要がある
		for i in range(1, n-l+2):
			# print("i: {}".format(i))
			j = i + l - 1 # lはウィンドウの長さ。
			# print("j: {}".format(j))
			# print("--------------------")
			m[i][j] = 100000000
			for k in range(i, j):
				m[i][j] = min(m[i][j], m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j])
	print(m[1][n])

if __name__ == '__main__':
	main()
